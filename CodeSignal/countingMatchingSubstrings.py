"""
You are given two strings - pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

Let's say that pattern matches a substring source[l..r] of source if the following three conditions are met:

they have equal length,
for each 0 in pattern the corresponding letter in the substring is a vowel,
for each 1 in pattern the corresponding letter is a consonant.
Your task is to calculate the number of substrings of source that match pattern.

Note: In this task we define the vowels as 'a', 'e', 'i', 'o', 'u', and 'y'. All other letters are consonants.

Example

For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
Expand to see the example video.

Note: If you are not able to see the video, use this link to access it.

"010" matches source[0..2] = "ama", because both 0s match a, which is a vowel, and 1 match m, which is a consonant;
"010" doesn't match source[1..3] = "maz", because the first 0 corresponds to an m, which is a consonant, not a vowel;
"010" matches source[2..4] = "azi", because the first 0 matches an a (vowel), 1 matches z (consonant), and the second 0 matches i (vowel);
"010" doesn't match source[3..5] = "zin", because the first 0 corresponds to a consonant (z);
"010" doesn't match source[4..6] = "ing", because the second 0 corresponds to the letter g, which is a consonant.
So, there are only 2 matches.

For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.

There are no double vowels in the string "codesignal", so it's not possible for any of its substrings to match this pattern.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string pattern

A string of 0s and 1s.

Guaranteed constraints:
1 ≤ pattern.length ≤ 103.

[input] string source

A string of lowercase English letters.

Guaranteed constraints:
1 ≤ source.length ≤ 103.

[output] integer

The number of substrings of source that match pattern.

"""

# SOLUTION
def solution(pattern, source):
    vowels = "aeiouy"
    matchCount = 0
    for i in range(len(source)-len(pattern)+1):
        substring = source[i:i+len(pattern)]
        
        
        if all((substring[j] in vowels and  pattern[j] =="0" ) or (substring[j] not in vowels and  pattern[j] =="1" )  for j in range(len(substring))):
            matchCount+=1
    return matchCount