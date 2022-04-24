//Runtime: 4 ms, faster than 80.95%
//Memory Usage: 43.8 MB, less than 50.61%

class Solution {
    public boolean isPalindrome(String s) {
        int l=0;
        int r = s.length()-1;
        while(l<=r){
            char a = s.charAt(l);
            char b = s.charAt(r);
            if (!Character.isAlphabetic(a) && !Character.isDigit(a)){
                l++;
            } else if (!Character.isAlphabetic(b) && !Character.isDigit(b)){
                r--;
            }
            else if (Character.compare(Character.toLowerCase(a),Character.toLowerCase(b))!=0){

                return false;
            }else{
              l++;
              r--;   
            }
        }
        return true;
    }
}