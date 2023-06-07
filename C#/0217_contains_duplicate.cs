// https://leetcode.com/problems/contains-duplicate/description/

public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var seen = new HashSet<int>();

        foreach (int i in nums)
        {
            if (seen.Contains(i)) 
            {
                return true;
            } else {
                seen.Add(i);
            }

        }
        return false;
    }
}
