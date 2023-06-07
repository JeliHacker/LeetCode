// https://leetcode.com/problems/valid-anagram/description/

public class Solution {
    public bool IsAnagram(string s, string t) {
        Dictionary<char, int> s_dict = new Dictionary<char, int>();

        foreach (char character in s) {
            if (s_dict.ContainsKey(character)) {
                s_dict[character] += 1;
            } else {
                s_dict[character] = 1;
            }
        }

        foreach (char character in t) {
            if (s_dict.ContainsKey(character) && s_dict[character] > 0) {
                s_dict[character] -= 1;
            } else {
                return false;
            }
        }

        foreach (char character in s) {
            if (s_dict[character] > 0){
                return false;
            }
        }

        return true;
    }
}
