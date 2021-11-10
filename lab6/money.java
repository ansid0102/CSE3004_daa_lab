import java.util.*;

public class money{
   
    static void moneyChange(int[] values){
        int[] deno= new int[] {10,5,1};
        int i,count,j = 0;
        while(j<=values.length){
            while(values[j]>0){
            if(deno[i]>values[j]){
                i+=1;
            }else{
                count+=1;
                System.out.println(deno[i]);
                values[j]-=deno[i];
            }
        }
        System.out.println("Min number of coins: "+count);
        j+=1;
        }
        
    }
}