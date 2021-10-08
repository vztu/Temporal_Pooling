from pooling import pooling

POOLING_TYPES = [
    'mean', 'geometric', 'median', 'harmonic',
    'minkowski', 'percentile', 'up-perc',
    'vqpooling', 'variation', 'recency', 'primacy',
    'hybrid', 'hysteresis', 'epool'
]

chunk = [8,8,9,9,10,10,9,9,5,5,6,6,7,7,8,8,10,10,2,2,
3,3,1,1,1,2,2,2,3,3,4,45,5,5,6,6,6,4,23,1,3,43,4,23,
43,2,30,2,1000,1222,2,2,2,2,2,2,]

print(f"Frame scores: {chunk}")
for pooling_type in POOLING_TYPES:
    val = pooling(chunk, pooling_type=pooling_type)
    print(f"{pooling_type}: {val}")


chunk = list(range(100))
print(f"\n\nFrame scores: {chunk}")
for pooling_type in POOLING_TYPES:
    val = pooling(chunk, pooling_type=pooling_type)
    print(f"{pooling_type}: {val}")