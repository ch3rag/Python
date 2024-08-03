import sys, re, codecs, copy
from bs4 import BeautifulSoup
from bs4.element import Tag

soup = None
head = None
body = None
diff = None
files = {}

# Static Resources
html = '<!DOCTYPE HTML><html lang="en"><head><title>Commit Details</title></head><body></body></html>'

styleSheets = [
    'https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/markdown.css',
    'https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/highlight.css',
    'https://fonts.googleapis.com/css2?family=Fira+Code:wght@300..700&display=swap',
    'Styles.css'
]

localStyleSheets = [
    # 'Styles.css'/
]

# Creates A HTML Tag
def createTag(name, content = None, attrs = None):
    tag = soup.new_tag(name)
    if isinstance(content, str):
        tag.string = content
    elif isinstance(content, int):
        tag.string = str(content)
    elif isinstance(content, Tag):
        tag.append(content)
    if attrs:
        for attr in attrs.keys():
            tag[attr] = attrs[attr]
    return tag

# Imports All StyleSheets
def importStyleSheets():
    for stylesheet in styleSheets:
        linkTag = createTag('link', attrs = {'rel': 'stylesheet', 'href': stylesheet})
        head.append(linkTag)
    for stylesheet in localStyleSheets:
        with open(stylesheet, 'r') as f:
            styleTag = createTag('style', f.read())
            head.append(styleTag)

# Creates A Table
def createTable(attrs = None):
    return createTag('table', attrs = attrs)

# Adds Header To Table
def addHeaderRow(table, cols, thAttrs = None, tdAttrs = None):
    th = createTag('thead', attrs = thAttrs)
    for col in cols:
        td = createTag('td', col, attrs = tdAttrs)
        th.append(td)
    table.append(th)

# Adds Row To Table
def addRow(table, cols, trAttrs = None, tdAttrs = None):
    tr = createTag('tr', attrs = trAttrs)
    for col in cols:
        td = createTag('td', col, attrs = tdAttrs)
        tr.append(td)
    table.append(tr)

# Returns Modification Type Tag
def getModificationTypeTag(fileData):
    if not 'Deleted' in fileData:
        return createTag('span', 'Deleted', {'class': 'deleted'})
    elif not 'Added' in fileData:
        return createTag('span', 'Added', {'class': 'added'})
    else:
        return createTag('span', 'Modified', {'class': 'modified'})

# Get File Type From Extension
def getFileType(fileName):
    if 'cls' in fileName:
        return 'Apex Class'
    elif 'md-meta' in fileName:
        return 'Metadata Record'
    elif 'field-meta' in fileName:
        return 'SObject/Metadata Field'

def renderFiles():
    changesContainer = createTag('div', attrs = {'class': 'changes-container'})
    changesContainer.append(createTag('h2', 'Changes Details'))

    for fileName, fileData in files.items():
        fileChangeContainer = createTag('div', attrs = {'class': 'file-change-container'})
        fileNameDiv = createTag('div', fileName, {'class': 'file-name'})
        diffCodeTablesContainer = createTag('div', attrs = {'class': 'code-tables-container tab-content'})
        oldCodeTablesContainer = createTag('div', attrs = {'class': 'code-tables-container tab-content'})
        newCodeTablesContainer = createTag('div', attrs = {'class': 'code-tables-container tab-content'})
        hiddenTab = createTag('pre', 'HIDDEN', attrs = {'class': 'code-tables-container tab-content hidden-tab'})

        fileChangeContainer.append(fileNameDiv)

        fileVersionTabs = createTag('div', attrs = {'class': 'tab'})
        diffLabel = createTag('label', 'Diff', {'for': f'chk-d-{fileName}', 'class': 'tab-links'})
        newLabel = createTag('label', 'New Version', {'for': f'chk-n-{fileName}', 'class': 'tab-links'})
        oldLabel = createTag('label', 'Old Version', {'for': f'chk-o-{fileName}', 'class': 'tab-links'})
        noneLabel = createTag('label', 'Hide All', {'for': f'chk-h-{fileName}', 'class': 'tab-links'})
        diffChk = createTag('input', attrs = {'id': f'chk-d-{fileName}', 'type': 'radio', 'name': fileName, 'checked': 'checked'})
        newChk = createTag('input', attrs = {'id': f'chk-n-{fileName}', 'type': 'radio', 'name': fileName})
        oldChk = createTag('input', attrs = {'id': f'chk-o-{fileName}', 'type': 'radio', 'name': fileName})
        hideChk = createTag('input', attrs = {'id': f'chk-h-{fileName}', 'type': 'radio', 'name': fileName})

        fileVersionTabs.append(diffLabel)
        fileVersionTabs.append(newLabel)
        fileVersionTabs.append(oldLabel)
        fileVersionTabs.append(noneLabel)

        fileChangeContainer.append(fileVersionTabs)

        if 'ObjectName' in fileData:
            fileNameDiv.string = fileData['ObjectName'] + '/' + fileNameDiv.text


        fileNameDiv.append(getModificationTypeTag(fileData))

        for change in fileData['Changes']:
            diffTable = createTable({'class': 'code-table'})
            oldTable = createTable({'class': 'code-table'})
            newTable = createTable({'class': 'code-table'})

            diffCodeTablesContainer.append(diffTable)
            oldCodeTablesContainer.append(oldTable)
            newCodeTablesContainer.append(newTable)

            oldVersion = f'Old Version: Start: { change['OldStart'] }, Lines: { change['OldCount'] }'
            newVersion = f'New Version: Start: { change['NewStart'] }, Lines: { change['NewCount'] }'

            
            oldVersionSpan = createTag('span', oldVersion, {'class': 'old-version-text'})
            newVersionSpan = createTag('span', newVersion, {'class': 'new-version-text'})

            span = createTag('span')
            span.append(oldVersionSpan)
            span.append(newVersionSpan)

            addHeaderRow(diffTable, ['L#', 'M', span])
            addHeaderRow(oldTable, ['L#', 'M', copy.copy(oldVersionSpan)])
            addHeaderRow(newTable, ['L#', 'M', copy.copy(newVersionSpan)])

            diffLineNumber = change['NewStart']
            newLineNumber = change['NewStart']
            oldLineNumber = change['OldStart']

            changeCounter = 0

            for line in change['Lines']:
                if len(line) > 0:
                    if line[0] == '-':
                        line = ' ' + line[1:]
                        addRow(diffTable, [diffLineNumber, createTag('span', '-'), createTag('pre', line)], tdAttrs = {'class': 'removed-line'})
                        addRow(oldTable, [oldLineNumber, createTag('span', '-'), createTag('pre', line)], tdAttrs = {'class': 'removed-line'})
                        changeCounter -= 1
                        oldLineNumber += 1
                    elif line[0] == '+':
                        line = ' ' + line[1:]
                        if changeCounter < 0:
                            diffLineNumber += changeCounter
                            changeCounter = 0
                        addRow(diffTable, [diffLineNumber, createTag('span', '+'), createTag('pre', line)], tdAttrs = {'class': 'added-line'})
                        addRow(newTable, [newLineNumber, createTag('span', '+'), createTag('pre', line)], tdAttrs = {'class': 'added-line'})
                        newLineNumber += 1
                    else:
                        if changeCounter < 0:
                            diffLineNumber += changeCounter
                            changeCounter = 0
                        preTag = createTag('pre', line)
                        addRow(diffTable, [diffLineNumber, ' ', preTag])
                        addRow(oldTable, [oldLineNumber, ' ', copy.copy(preTag)])
                        addRow(newTable, [newLineNumber, ' ', copy.copy(preTag)])
                        oldLineNumber += 1
                        newLineNumber += 1
                else:
                    if changeCounter < 0:
                        diffLineNumber += changeCounter
                        changeCounter = 0

                    preTag = createTag('pre', line)
                    addRow(diffTable, [diffLineNumber, ' ', preTag])
                    addRow(oldTable, [oldLineNumber, ' ', copy.copy(preTag)])
                    addRow(newTable, [newLineNumber, ' ', copy.copy(preTag)])
                    oldLineNumber += 1
                    newLineNumber += 1
                diffLineNumber += 1
        fileChangeContainer.append(diffChk)
        fileChangeContainer.append(diffCodeTablesContainer)
        fileChangeContainer.append(oldChk)
        fileChangeContainer.append(oldCodeTablesContainer)
        fileChangeContainer.append(newChk)
        fileChangeContainer.append(newCodeTablesContainer)
        fileChangeContainer.append(hideChk)
        fileChangeContainer.append(hiddenTab)
        changesContainer.append(fileChangeContainer) 
    body.append(changesContainer)

# Adds Changes Summary
def addChangesSummary():
    body.append(createTag('h2', 'Changes Summary'))
    table = createTable({'class': 'changes-summary-table'})
    addHeaderRow(table, ['Sr.', 'File Name', 'File Type', 'Object Name', 'Modification Type'])
    i = 1
    for fileName, fileData in files.items():
        objName = 'N/A'
        if 'ObjectName' in files[fileName]:
            objName = files[fileName]['ObjectName']
        addRow(table, [i, fileName, getFileType(fileName), objName, getModificationTypeTag(fileData)])
        i += 1
    body.append(table)

# Populates Files Dict
def populateFiles():
    newFileNameRe = r'[+]{3} b.*?([A-Za-z_]+(\.[a-zA-Z1-9_-]+){1,})'
    oldFileNameRe = r'[-]{3} a.*?([A-Za-z_]+(\.[a-zA-Z1-9_-]+){1,})'
    objectNameRe = r'objects\/([A-Za-z_]+(__c|__mdt))'
    chunkRe = re.compile(r'@@\s-(\d+),(\d+)\s\+(\d+),(\d+)\s@@')
    diffRe = r'diff\s--git\sa/.*?b/.*'

    inCode = False
    i = 6
    while i < len(diff):
        line = diff[i]

        newFileNameMatch = re.search(newFileNameRe, line)
        oldFileNameMatch = re.search(oldFileNameRe, line)
        chunkReMatch = re.search(chunkRe, line)
        diffReMatch = re.search(diffRe, line)

        if diffReMatch:
            inCode = False

        elif oldFileNameMatch or newFileNameMatch:
            newFileName = newFileNameMatch.group(1) if newFileNameMatch else None
            oldFileName = oldFileNameMatch.group(1) if oldFileNameMatch else None

            fileName = newFileName or oldFileName
            if not fileName in files:
                files[fileName] = {}
                objectNameMatch = re.search(objectNameRe, line)
                if objectNameMatch:
                    objectName = objectNameMatch.group(1)
                    files[fileName]['ObjectName'] = objectName
                files[fileName]['Changes'] = []

            fileData = files[fileName]

            if oldFileNameMatch:
                fileData['Added'] = False

            if newFileNameMatch:
                fileData['Deleted'] = False

        elif chunkReMatch:
            oldStart, oldCount = int(chunkReMatch.group(1)), int(chunkReMatch.group(2))
            newStart, newCount = int(chunkReMatch.group(3)), int(chunkReMatch.group(4))
            changeDict = {}
            changeDict['OldStart'] = oldStart
            changeDict['OldCount'] = oldCount
            changeDict['NewStart'] = newStart
            changeDict['NewCount'] = newCount
            changeDict['Lines'] = []
            files[fileName]['Changes'].append(changeDict)
            inCode = True

        elif inCode:
            files[fileName]['Changes'][-1]['Lines'].append(line)

        i += 1

# Add Commit Details
def addCommitHeader():
    commitHeaderDivContainer = createTag('div', attrs = {'class': 'commit-header'})
    commitId = re.search(r'commit\s(.*)', diff[0]).group(1)
    authorName = re.search(r'Author:\s(.*)', diff[1]).group(1)
    commitDate = re.search(r'Date:\s+(.*)', diff[2]).group(1)
    commitName = diff[4].strip()

    table = createTable({'class': 'commit-header-table'})
    addRow(table, ['Author:', authorName])
    addRow(table, ['Commit Date:', commitDate])
    addRow(table, ['Commit SHA:', commitId])

    commitHeaderDivContainer.append(createTag('h1', commitName))
    commitHeaderDivContainer.append(table)
    body.append(commitHeaderDivContainer)

def writeToFile(fileName):
    with open(fileName, 'w', encoding = 'utf-8') as f:
        f.write(str(soup.prettify()))


# Main
def main():
    global html
    global soup
    global body
    global head
    global diff

    if (len(sys.argv) != 3):
        print('USAGE: python DiffMDFormatter.py <Input FileName> <Output Filename>')
        return

    inStream = codecs.open(sys.argv[1], 'r', encoding='utf-16-le')
    diff = []
    for line in inStream:
        diff.append(line.rstrip())

    soup = BeautifulSoup(html, features = "lxml")
    head = soup.head
    body = soup.body

    importStyleSheets()
    addCommitHeader()
    populateFiles()
    addChangesSummary()
    renderFiles()
    writeToFile(sys.argv[2])

# Main
if __name__ == '__main__':
    main()
