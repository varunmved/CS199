#include <stdio.h>

int length(char *in){
    int i =0;
    while(in[i]!= '\0'){
        i++;
    }
    
    return i;
}

int isTrue(char* a, char*b)
{
    int j = 0;
    for(int i = 0; i<length(a)&& j<length(b);i++){
            if(a[i] == b[j])
            {
                j++;
            }
    }
    
    if(j == length(b))
    {
        return 1;
    }
    return 0;

}

int main()
{
    char * a = "xxx";
    char * b = "oxoxoxo";
    int result = -1;

    result = isTrue(a,b);
    printf("%d",result);
    //return 0;
}
