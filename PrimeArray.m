%primeArray = myNPrimes(1013278);
upper = sym(800800)^800800;
%outerPrime = vec(1:35416);
%outerPrime = outerPrime';
%vecJ = vec(7:length(vec));
%vecJ = flip(vecJ);
%vecJ = vecJ';
%PrimeCount = length(vecJ);

count = 0;

a = datetime;

for i = outerPrime
    vecJ = vecJ(1:length(vecJ)-1);
    PrimeCount = length(vecJ);
    for j = vecJ
            if (sym(i)^j*sym(j)^i) > upper
                PrimeCount = PrimeCount - 1;
            else
                count = count + PrimeCount;
                break
            end
    end
end
b = datetime;
disp(b-a)

load handel;
disp(count)
sound(y,Fs)