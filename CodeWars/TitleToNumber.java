public class TitleToNumber {
    public static void main(String[] args){
        System.out.println(args[0]);
        System.out.println(titleToNumber(args[0]));
        }
        public static long titleToNumber(String title) {
            int length = title.length(), j;
            long result = 0;
            j = length;
            for(int i = 0; i < length; i++){
                char c = title.charAt(i);
                result += (long)(Math.pow(26,j-1))*(c - 'A' + 1) ;
                j--;
                }
            return result;

            }
        }
