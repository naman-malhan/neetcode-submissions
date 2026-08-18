class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0 : return ''
        finalEncodedStr = ''
        for word in strs:
            finalEncodedStr += str(len(word)) + '#' + word
        print(finalEncodedStr, "finalEncodedStr")
        return finalEncodedStr

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []

        decodedList = []
        currentIndex = 0

        while currentIndex < len(s):
            delimiterIndex = currentIndex

            # Find '#'
            while s[delimiterIndex] != '#':
                delimiterIndex += 1

            # Extract word length
            wordLength = int(s[currentIndex:delimiterIndex])

            # Move to beginning of word
            currentIndex = delimiterIndex + 1

            # Find end of word
            wordIndex = currentIndex + wordLength

            # Extract word
            decodedList.append(s[currentIndex:wordIndex])

            # IMPORTANT: move to next encoded word
            currentIndex = wordIndex

        return decodedList