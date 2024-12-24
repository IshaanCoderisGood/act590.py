def reverse(a, a_size, n):
    temp = 0
    while (temp<a_size):
        start = temp
        end = min(temp + n - 1, a_size - 1)
        while (start<end):
         a[start], a[end] = a[end], a[start]
         start += 1
         end -= 1
        temp +=n
a = [5,48,494,4913,48914894891489149889148941,4894189471947298479817948791874917491749847914874198741987419874198741984719874987489748957589759858953928,58948294298248942894284285729875295729825789527598275298751015709275092785298725927219752190]
a_size = len(a)
n = 2
reverse(a, a_size, n)
for i in range(0, a_size):
    print(a[i], end=",")