# 资料来源与解释边界

公开页面核对日期：2026-09-11。只链接来源，不复制整篇论文或第三方图片。

| 材料 | 作者或维护者／年份 | 本项目使用范围 |
|---|---|---|
| [Euclid's Elements IX.20](https://mathcs.clarku.edu/~djoyce/elements/bookIX/propIX20.html) | 欧几里得；David E. Joyce维护的大学页面，古典命题 | Issue 002构造证明的来源，正文用现代中文教学表述 |
| [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Ashish Vaswani等，2017；页面所列v7修订于2023 | Issue 001采用第3.2.1节公式完成单查询计算演示；不是完整训练实验复现 |
| [Learn Lean](https://lean-lang.org/learn/) | Lean官方学习资源页，动态更新 | Issue 003后续Lean 4入门入口；尚未运行Lean检查。当前Python多项式演示独立于Lean |
| [GPT-6 Astra官方页面](https://openai.com/index/gpt-6-astra/) | OpenAI，2026；脚注9 | 核对short prime gaps的186官方描述及Proof、supporting research入口；官方发布不等于独立同行评审 |
| [PrimeGaps186](https://github.com/openai/PrimeGaps186) | OpenAI；本次核对提交`61340d0b74163003b32756bb16e91d9209a5e330` | 核对DHL[40,2]、相邻素数间距目标、Lean主要结果、显式输入、Python/FLINT证书及验证边界 |
| [Bounded prime gap constant](https://teorth.github.io/optimizationproblems/constants/88a.html) | Terence Tao / Optimization Problems，动态条目 | 交叉定位246、240、186与DHL[40,2]；贡献说明披露AI辅助整理且未独立验证上界，不作为核心事实的唯一证据 |
| [Bounded gaps between primes](https://arxiv.org/abs/2608.31126) | Julia Stadlmann，2026-08-31，预印本摘要 | 从作者原始摘要确认246背景及H₁≤240；未下载或复制论文全文 |

上述新增来源用于[素数间隔前沿桥接卡](frontier-bridge-prime-gaps.md)，核对日期为2026-09-11。PrimeGaps186的[README](https://github.com/openai/PrimeGaps186/blob/61340d0b74163003b32756bb16e91d9209a5e330/README.md)、[formalization.yaml](https://github.com/openai/PrimeGaps186/blob/61340d0b74163003b32756bb16e91d9209a5e330/formalization.yaml)与[比较器配置](https://github.com/openai/PrimeGaps186/blob/61340d0b74163003b32756bb16e91d9209a5e330/comparator/main.json)分别用于核对公开说明、目标级零`sorry`及审阅状态、获准公理集合。未重跑外部Lean构建或数值证书；不将零`sorry`扩大为所有输入均已在Lean证明，也不将186写成孪生素数结论。

工作设想中的部门衔接依据竞聘者提供的创新实践部招新介绍：赛事通知与材料跟进、大创申报与结题跟进、特色实践活动和科创讲座。此处是工作设想，不是对学院最新政策或赛事规则的独立公告。

内容和代码采用AI辅助起草；验算与测试是有限范围的软件检查，不替代教师审阅，也不证明展示者已独立掌握内容。公开开展前，应由展示者通读、试讲、核对来源并寻求适当审阅。
