import tensorflow as tf
print(tf.__version__)

from ai_benchmark import AIBenchmark
benchmark = AIBenchmark()
results = benchmark.run()