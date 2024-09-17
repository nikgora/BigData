4\
Результат роботи \
Складність роботи Стандартного алгоритма О(n).\
Судячи з результатів заміру швидкості роботи складність роботи вбудованого методу пошуку максимуму О(n/2). Бо завжди +- у 2 рази він швидше ніж прохід по всім елемеентам масива \
***Приклади***\
Enter the number of elements in the array: 100000000\
Enter the number of processes for MapReduce (maximum 12): 10\
Max value (max(arr)): 8412931090127, Time: 1.0965943336486816 seconds\
Max value (standard): 8412931090127, Time: 2.02459979057312 seconds\
Time for splitting into chunks: 0.4633002281188965 seconds\
Time for processing chunks: 9.026177167892456 seconds\
Max value (MapReduce): 8412931090127, Time: 9.910645484924316 seconds, Time without splitting: 9.44734525680542 seconds\
\
\
Enter the number of elements in the array: 10000000\
Enter the number of processes for MapReduce (maximum 12): 10\
Max value (max(arr)): 8412931130510, Time: 0.10651707649230957 seconds\
Max value (standard): 8412931130510, Time: 0.20202255249023438 seconds\
Time for splitting into chunks: 0.043003082275390625 seconds\
Time for processing chunks: 0.9677262306213379 seconds\
Max value (MapReduce): 8412931130510, Time: 1.050729751586914 seconds, Time without splitting: 1.0077266693115234 seconds\
\
\
Enter the number of elements in the array: 1000000\
Enter the number of processes for MapReduce (maximum 12): 10\
Max value (max(arr)): 8412908307856, Time: 0.010995149612426758 seconds\
Max value (standard): 8412908307856, Time: 0.020000457763671875 seconds\
Time for splitting into chunks: 0.003998517990112305 seconds\
Time for processing chunks: 0.2682180404663086 seconds\
Max value (MapReduce): 8412908307856, Time: 0.27721667289733887 seconds, Time without splitting: 0.27321815490722656 seconds\
\
Швидкість розбиття масиву на чанки десь 1/4 - 1/5 часу від лінійного однопоточного знаходження максимума, цей час не залежить від кількості процесів, бо він однопоточний.\
На моєму комп'ютері реалізація MapReduce відбуваєтьмя повільніше, бо доволі багато процесів відбуваютсья в фоні, і коли створюються нові процеси вони не пріотеризовані виконуватися одразу, що критично впливає на швидкість виконання.

