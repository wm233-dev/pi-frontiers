# v0.1 验证记录

日期：2026-09-11。环境：Windows，Python 3.14，标准库。代码目标兼容Python 3.10及以上；本次未逐版本运行。

实际执行：

```sh
python demo/primes.py
python -m unittest discover -s tests -v
```

脚本输出：

```text
primes=[2, 3]
product+1=7; prime_factors=[7]
all factors outside input: True

primes=[2, 3, 5, 7, 11, 13]
product+1=30031; prime_factors=[59, 509]
all factors outside input: True

primes=[3, 5]
product+1=16; prime_factors=[2, 2, 2, 2]
all factors outside input: True

Finite examples only; see the written proof in the guide.
```

5项unittest全部通过：

1. 已知素数、合数与0、1、负数边界。
2. 30031=59×509的反例。
3. 重复素因子及新素因子可能较小的情况。
4. 前六个素数的全部63个非空子集：因子乘积回算、与原列表互异，并以完整因子范围独立检查素性。
5. 空列表、重复值、合数、超出教学范围、布尔值和非整数等无效输入。

测试证明这些有限计算与输入处理符合预期，不替代一般性数学证明。没有实际活动记录、教师审核记录或展示者试讲记录；AI与数学交叉的Lean验证仍为后续计划。
