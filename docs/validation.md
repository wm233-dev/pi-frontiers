# v0.2 验证记录

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

原有素数演示的5项unittest全部通过：

1. 已知素数、合数与0、1、负数边界。
2. 30031=59×509的反例。
3. 重复素因子及新素因子可能较小的情况。
4. 前六个素数的全部63个非空子集：因子乘积回算、与原列表互异，并以完整因子范围独立检查素性。
5. 空列表、重复值、合数、超出教学范围、布尔值和非整数等无效输入。

## v0.2 新增演示和回归检查

实际执行`python demo/attention.py`、`python demo/identity_checker.py`以及完整unittest测试集，**共12项测试全部通过**。

注意力演示的关键输出：

| Query | 权重（保留6位小数） | 输出（保留6位小数） |
|---|---|---|
| [1,0] | [0.669762,0.330238] | [6.697615,6.604769] |
| [0,1] | [0.330238,0.669762] | [3.302385,13.395231] |
| [0,0] | [0.5,0.5] | [5,10] |

新增4项注意力测试检查公式预期值、等权/单项和softmax平移不变性、键值成对置换不变性、维数与非有限值等无效输入。程序限制小数组，分数超出教学范围会报错，不宣称覆盖任意大矩阵。

恒等式演示：正确展开式返回`identity=True`；漏掉2x的式子返回`identity=False`并找到x=−3的反例。七个整数抽样点均为0的多项式返回：

```text
{'identity': False, 'difference': {7: 1, 5: -14, 3: 49, 1: -36}, 'counterexample': None}
```

新增3项恒等式测试覆盖已知系数与恒等式、错误命题与抽样陷阱、语法和范围拒绝。表达式解析没有使用`eval`；不支持分式、多变量、函数调用或任意证明。`counterexample`只在−3至3搜索，找不到不等于结论成立；恒等判断依据精确多项式系数。

这些检查验证了演示的约定行为，不替代正式证明助手、教师审核或实际教学反馈。没有实际活动记录、教师审核记录或展示者试讲记录；Lean验证仍为后续计划。
