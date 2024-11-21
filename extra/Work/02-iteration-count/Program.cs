// This is in response to https://youtu.be/uqpA6wySe8o?t=1637
// code was like C/C++ so I used CSharp

int count = 0;
int count_i = 0;
int count_j = 0;
int count_less = 0;
int count_equals = 0;
int number_of_zerosums = 0;

var numbers = new List<int> {-1, 0, 9, 1, 3, -9, 0, -3};
int N = numbers.Count();

for (int i = 0; i < N; i++)
{
    count_less++;
    count_i++;
    for (int j = i + 1; j < N; j++)
    {
        count_less++;
        count_j++;
        count_equals++;
        if (numbers[i] + numbers[j] == 0){
            number_of_zerosums++;
        }
    }


}


Console.WriteLine($"N = {N}");
Console.WriteLine($"Iterations on i {count_i}"); /* N */
Console.WriteLine($"Iterations on j {count_j}");   /* */
Console.WriteLine($"Number of times < was used: {count_less}");
Console.WriteLine($"Number of times == was used: {count_equals}");
Console.WriteLine($"Number of ZeroSums: {number_of_zerosums}");