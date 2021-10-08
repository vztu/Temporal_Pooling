# Temporal_Pooling
Implementation of temporal pooling methods studied in [ICIP'20] A Comparative Evaluation Of Temporal Pooling Methods For Blind Video Quality Assessment

## Requirements

* numpy, scipy, sklean

## Test

`python3 test.py`

```
Frame scores: [8, 8, 9, 9, 10, 10, 9, 9, 5, 5, 6, 6, 7, 7, 8, 8, 10, 10, 2, 2, 3, 3, 1, 1, 1, 2, 2, 2, 3, 3, 4, 45, 5, 5, 6, 6, 6, 4, 23, 1, 3, 43, 4, 23, 43, 2, 30, 2, 1000, 1222, 2, 2, 2, 2, 2, 2]
mean: 47.464285714285715
geometric: 5.888227387333425
median: 5.0
harmonic: 3.420682754863689
minkowski: 211.392998937997
percentile: 1.0
up-perc: 303.625
vqpooling: 46.913926267214485
variation: 374.3333333333333
recency: 2.0
primacy: 8.986667555478524
hybrid: 47.77485231254695
hysteresis: 27.1638829291158
epool: [47.464285714285715, 211.392998937997, 1.0, 46.913926267214485, 374.3333333333333, 27.1638829291158]


Frame scores: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
mean: 49.5
geometric: 37.62310047409743
median: 49.5
harmonic: 19.121649843516597
minkowski: 57.301832431432764
percentile: 4.5
up-perc: 89.5
vqpooling: 40.105642912001294
variation: 0
recency: 96.52916486820983
primacy: 2.4708351317901758
hybrid: 49.459016154756526
hysteresis: 49.20040871424151
epool: [49.5, 57.301832431432764, 4.5, 40.105642912001294, 0, 49.20040871424151]
```