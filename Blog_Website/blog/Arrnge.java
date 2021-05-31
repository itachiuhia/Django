import java.util.*;

class Arrange{
    public static void main(String[] args) {
        int t = 6;
        int[] arr = {1, 9, 2, 4, 0, 3};
        System.out.println(checkConsucutive(t, arr));
      System.out.print( Solution("aaabbb"));
    }

    public static int checkConsucutive(int input1, int[] input2){
        Arrays.sort(input2);

        for(int i=1; i<input1; i++){
           int  diff = input2[i]-input2[i-1];
            if(diff != 1){
                return 0;
            }
        }
        return 1;
        
    }

    public static  int  Solution(String S){
                char[] str = S.toCharArray();
                int N = S.length();
                HashMap<Character, Integer> mp = new HashMap<>(); 
                PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> Integer.compare(y, x));                
                int cntChar = 0;                
                for (int i = 0; i < N; i++)
                {
                    if(mp.containsKey(str[i]))
                    {
                    mp.put(str[i],
                    mp.get(str[i]) + 1);
                    }
                    else
                    {
                    mp.put(str[i], 1);
                    }
                }                
                for (Map.Entry<Character, Integer> it : mp.entrySet())
                {
                    pq.add(it.getValue());
                }
                while (!pq.isEmpty())
                {   int frequent = pq.peek();
                    pq.remove();
                
                    if (pq.isEmpty()) {                
                      return cntChar;
                    }
                
                    if (frequent == pq.peek())
                    {
                    
                    if (frequent > 1)
                    {
                         pq.add(frequent - 1);
                    }                
                    cntChar++;
                    }
                }                
                return cntChar;
            }

    private static int minOccur(char[] str, int N) {
    HashMap<Character, Integer> mp = new HashMap<>();        
        PriorityQueue<Integer> pq = new PriorityQueue<>((x, y) -> Integer.compare(y, x));
        
        int cntChar = 0;
        
        for (int i = 0; i < N; i++)
        {
            if(mp.containsKey(str[i]))
            {
            mp.put(str[i],
            mp.get(str[i]) + 1);
            }
            else
            {
            mp.put(str[i], 1);
            }
        }
        
        for (Map.Entry<Character, Integer> it : mp.entrySet())
        {
            pq.add(it.getValue());
        }

        while (!pq.isEmpty())
        {
            
            int frequent = pq.peek();
        
            pq.remove();
        
            if (pq.isEmpty()) {
        
            return cntChar;
            }
        
            if (frequent == pq.peek())
            {
            
            if (frequent > 1)
            {
            
                pq.add(frequent - 1);
            }
        
            cntChar++;
            }
        }
        
        return cntChar;

    }

    // private static int countSetBits(int k) {

        
        
    // }
}

// int n = inputByLine.get(0);
// String str = inputByLine.get(1);
// int hops = 1;
// int h = 1;
// for(Char c : str.toCharArray()){
    
//     if( c == '1'){
//         if(h > 1){
//             if(h > hops){
//                 hops = h;
//                 h = 1;
//             }
//         }
        
//     }
//     else if(c == '0'){
//         hop += 1;
//     }
// }
// System.out.println(hops);
