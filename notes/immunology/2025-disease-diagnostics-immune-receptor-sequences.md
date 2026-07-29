# Disease diagnostics using machine learning of B cell and T cell receptor sequences

## 本文目录

- [基本信息](#基本信息)
- [本论文主图](#本论文主图)
- [生物学故事前情](#生物学故事前情)
- [重要缩写表](#重要缩写表)
- [论文详细解读](#论文详细解读)
- [研究问题与科学背景](#研究问题与科学背景)
- [研究设计与数据结构](#研究设计与数据结构)
- [方法与整体框架](#方法与整体框架)
- [原文结果完整梳理](#原文结果完整梳理)
  - [Integrated repertoire models of immune states](#integrated-repertoire-models-of-immune-states)
  - [Limited impact of batch effects on classification](#limited-impact-of-batch-effects-on-classification)
  - [Limited impact of age, sex, and race on classification](#limited-impact-of-age-sex-and-race-on-classification)
  - [Language model recapitulates immunological knowledge](#language-model-recapitulates-immunological-knowledge)
- [原文讨论中的主要结论](#原文讨论中的主要结论)
- [作者结论与证据强度](#作者结论与证据强度)
- [独立方法学详解](#独立方法学详解)
  - [样本与测序](#样本与测序)
  - [序列预处理与 clonal lineage 压缩](#序列预处理与-clonal-lineage-压缩)
  - [模型 1：repertoire composition classifier](#模型-1：repertoire-composition-classifier)
  - [模型 2：CDR3 convergent clustering classifier](#模型-2：cdr3-convergent-clustering-classifier)
  - [模型 3：language model embedding classifier](#模型-3：language-model-embedding-classifier)
  - [统计学分析方法](#统计学分析方法)
  - [集成模型和数据泄漏控制](#集成模型和数据泄漏控制)
  - [稳健性验证和混杂控制](#稳健性验证和混杂控制)
- [生物学与临床意义](#生物学与临床意义)
- [局限性与危险假设](#局限性与危险假设)
- [深度研究洞察](#深度研究洞察)
- [可借鉴或迁移的思路](#可借鉴或迁移的思路)
- [可复用学术表达](#可复用学术表达)
- [相关论文与概念](#相关论文与概念)

## 基本信息

- 原文题名：Disease diagnostics using machine learning of B cell and T cell receptor sequences
- 期刊：Science 387, eadp2407
- 年份：2025
- DOI：10.1126/science.adp2407
- 第一作者：Maxim E. Zaslavsky、Erin Craig
- 通讯作者：Anshul Kundaje、Scott D. Boyd
- 研究领域：免疫受体组学、机器学习诊断、感染性疾病、自身免疫病、BCR/TCR repertoire
- 关键词：BCR、TCR、免疫受体库、Mal-ID、ESM-2、CDR3、系统性红斑狼疮、1 型糖尿病、COVID-19、HIV、流感疫苗
- PDF 解析质量：正文、方法、图注、参考文献、数据可用性信息可解析；主文补充表格和补充图仅在正文中被引用，未作为完整表格对象嵌入主 PDF。
- 重要数字提示：原文在研究摘要处写健康对照为 220 人，在方法处写健康对照为 217 人；本文保留该不一致，不自行修正。

## 本论文主图

| 原文图 | 原文图题/核心信息 | 是否截取 | 图像文件 | 放置位置 |
|---|---|---|---|---|
| 图 1 | Mal-ID framework：BCR/TCR 测序、三类模型、集成预测、生物学验证和临床阈值应用 | 是 | `assets/immunology/2025-disease-diagnostics-immune-receptor-sequences/fig1-mal-id-framework.png` | [方法与整体框架](#方法与整体框架) |
| 图 2 | Mal-ID classifies disease using IgH and TRB sequences：六类免疫状态分类、模型组件比较、狼疮诊断阈值 | 是 | `assets/immunology/2025-disease-diagnostics-immune-receptor-sequences/fig2-classification-performance.png` | [Integrated repertoire models of immune states](#integrated-repertoire-models-of-immune-states) |
| 图 3 | Disease-associated IGHV genes and isotypes prioritized by model 3 using protein language embeddings：模型 3 的 IGHV/同种型 SHAP 解释 | 是 | `assets/immunology/2025-disease-diagnostics-immune-receptor-sequences/fig3-ighv-isotype-shap.png` | [Language model recapitulates immunological knowledge](#language-model-recapitulates-immunological-knowledge) |
| 图 4 | Models 2 and 3 learn SARS-CoV-2 antigen-specific sequence patterns：外部 SARS-CoV-2 结合抗体序列验证 | 是 | `assets/immunology/2025-disease-diagnostics-immune-receptor-sequences/fig4-known-sars-cov-2-binders.png` | [Language model recapitulates immunological knowledge](#language-model-recapitulates-immunological-knowledge) |

## 生物学故事前情

适应性免疫系统本质上是一套“抗原暴露记录仪”。B 细胞和 T 细胞在感染、疫苗接种、自身免疫和慢性炎症中经历克隆选择，留下 V/J 基因使用、CDR3 序列、同种型、体细胞突变和克隆扩增等痕迹。传统诊断通常检测病原体、抗体浓度或炎症指标，但很少直接利用整套 BCR/TCR repertoire 作为疾病状态读数。

难点在于，免疫受体库极其稀疏和个体化。两个患者面对相似抗原时，可能没有完全相同的 CDR3；同一患者体内，与疾病直接相关的克隆也可能只占很小部分。BCR 还会经历 SHM 和同种型转换，TCR 又受 HLA 背景强烈影响。因此，简单找公共克隆太窄，直接把所有序列喂给模型又容易学到批次、年龄、祖源或疾病严重程度等混杂。

本文的生物学故事是把 immune repertoire 从“序列数据库”提升为“疾病状态的多层级表型”。作者用整体组成、CDR3 收敛聚类和蛋白语言模型三种视角，同时读取 BCR 和 TCR 的信息，并追问这些序列模式能否区分感染、自身免疫、疫苗反应和健康状态。

## 重要缩写表

| 缩写 | 中文含义 | 本文语境中的具体指代 | 阅读时注意 |
|---|---|---|---|
| Mal-ID | machine learning for immune diagnosis | 本文提出的 BCR/TCR 多模型疾病诊断框架 | 是研究框架，不是单一算法 |
| BCR | B 细胞受体 | IgH 序列和同种型信息构成的 B 细胞 repertoire | BCR 信号可能反映抗原特异性，也可能反映免疫状态 |
| TCR | T 细胞受体 | TRB 序列构成的 T 细胞 repertoire | TCR 识别受 HLA 限制，跨人群公共模式更难 |
| IgH | 免疫球蛋白重链 | BCR heavy chain 测序对象 | 本文不是完整抗体轻重链配对 |
| TRB | TCR beta chain | TCR beta 链测序对象 | beta 链不能完整确定 TCRαβ 特异性 |
| CDR3 | 互补决定区 3 | BCR/TCR 中最常用于定义克隆和抗原识别模式的区域 | 相似 CDR3 只是候选功能相似，不等于已验证结合 |
| ESM-2 | 蛋白语言模型 | 将 CDR3 氨基酸序列转为 embedding 的模型 | embedding 捕捉统计模式，不直接解释生物机制 |
| AUROC | ROC 曲线下面积 | 衡量疾病分类排序能力 | 高 AUROC 不等于临床阈值已确定 |
| AUPRC | precision-recall 曲线下面积 | 用于不平衡任务和 binder 富集评价 | 受阳性比例影响，需和基线比较 |
| SHAP | Shapley additive explanations | 解释模型 3 中 V gene/isotype 等特征对预测的贡献 | 解释模型行为，不证明因果 |
| SLE | 系统性红斑狼疮 | 本文自身免疫病分类任务之一 | 疾病活动度和治疗状态会影响 repertoire |
| T1D | 1 型糖尿病 | 本文自身免疫病分类任务之一 | 队列年龄结构可能与其他疾病类别不同 |

## 论文详细解读

### 研究问题与科学背景

传统临床诊断主要依赖症状、体征、常规实验室检查、影像学、病原体检测和自身抗体检测。对于感染性疾病，病原体本身常常可以作为诊断锚点；但对于系统性红斑狼疮、1 型糖尿病等自身免疫病，临床诊断通常依赖多种不完全特异的证据组合，过程长、误诊风险高，而且不同疾病之间常有症状重叠。

作者提出的关键科学问题是：B 细胞受体和 T 细胞受体是否可以作为机体抗原暴露和免疫反应历史的“内源性记录”，用于同时识别多种感染、疫苗反应、自身免疫病和健康状态。这个问题困难在于，BCR/TCR 序列高度多样，每个患者体内真正与疾病相关的克隆可能只占很小比例；BCR 还存在体细胞高突变；TCR 识别又受到 HLA 背景影响。单纯寻找完全相同的公共克隆容易漏掉信号，单纯看总体组成又容易把年龄、祖源、批次或炎症背景误认为疾病。

因此，这篇文章真正要解决的是“免疫受体库如何表示”的问题。作者不是把 receptor repertoire 当成一堆序列直接分类，而是构建了一个多层级框架：整体组成、CDR3 收敛聚类、蛋白语言模型嵌入，再将 BCR 和 TCR 两条免疫轴整合起来。

### 研究设计与数据结构

作者构建并分析了 593 名个体的免疫受体数据，疾病或免疫状态包括 COVID-19、HIV 感染、系统性红斑狼疮、1 型糖尿病、流感疫苗接种后状态和健康对照。原文报告共有 542 名个体具有配对 IgH 和 TRB 序列数据。数据规模为 1620 万个 BCR heavy chain clone 和 2350 万个 TCR beta chain clone。

队列设计上，作者有意纳入异质性较强的状态：急性感染、慢性感染、疫苗刺激、自身免疫病和健康背景。这使任务不是简单的“疾病 versus 健康”，而是多疾病免疫状态分类。方法学上，所有个体按人而不是按序列分入训练集、验证集和测试集；同一个人的重复样本必须放在同一个划分内。这一点非常关键，因为同一个人的 repertoire 内部高度相关，如果把同一个人的序列拆到训练和测试两侧，会严重高估模型性能。

作者还设置了外部验证：用其他实验室的 COVID-19 与健康 BCR/TCR 数据测试模型泛化；并在 Adaptive Biotechnologies 的 genomic DNA TCR 数据上重新训练框架，以评估该方法是否能跨测序技术扩展。总体上，研究设计比一般 repertoire 机器学习论文更重视数据泄漏、批次效应和人口学混杂。

### 方法与整体框架

![图1：Mal-ID整体框架](../../assets/immunology/2025-disease-diagnostics-immune-receptor-sequences/fig1-mal-id-framework.png)

图 1 展示了 Mal-ID 的基本逻辑。作者从外周血中扩增并测序 BCR heavy chain 和 TCR beta chain，然后分别训练三类模型。模型 1 使用 repertoire composition，也就是 V/J 基因使用频率以及 BCR 的体细胞高突变等总体特征。模型 2 使用 CDR3 聚类，寻找不同个体中高度相似、并在特定疾病中富集的候选公共或收敛克隆。模型 3 使用蛋白语言模型 ESM-2 将 CDR3 氨基酸序列转化为 640 维嵌入，再训练序列层面和样本层面的疾病预测模型。

这三个模型分别对应不同生物学层级。模型 1 捕捉整体免疫组成和克隆选择造成的分布改变；模型 2 捕捉跨个体共享的候选抗原特异性序列；模型 3 捕捉不一定序列完全相同、但可能在结构或结合性质上相似的 receptor pattern。最后，作者把三类 BCR 模型和三类 TCR 模型输入一个 logistic regression 集成模型，输出每个疾病状态的概率。

模型 3 的标签设计需要特别注意。作者并不知道每条 BCR/TCR 序列是否真正和疾病相关，因此单条序列继承患者疾病标签。这是一种弱监督学习：标签有噪声，但在大规模序列和分层聚合下，疾病相关信号可能从噪声中显现。这个设定也决定了后文解释必须谨慎：模型可能学到直接抗原特异性序列，也可能学到更宽泛的疾病相关免疫状态。

### 原文结果完整梳理

#### Integrated repertoire models of immune states

![图2：Mal-ID多疾病分类结果](../../assets/immunology/2025-disease-diagnostics-immune-receptor-sequences/fig2-classification-performance.png)

原文首先报告，Mal-ID 在 550 个配对 BCR/TCR 测试样本、542 名个体中实现六类免疫状态分类，multiclass AUROC 为 0.986。图 2A 的混淆矩阵显示，当按最高预测概率直接给出类别标签时，总体准确率为 85.3%。这说明模型具有很强的排序能力，但并不是每个样本都能被完全正确归类。这个区别很重要：AUROC 衡量的是正负样本排序能力，而临床诊断最终还需要阈值和类别决策。

图 2B 比较了不同模型组件。单独使用 CDR3 聚类的模型性能较弱，BCR CDR3 聚类 AUROC 为 0.89，TCR CDR3 聚类 AUROC 为 0.80。相比之下，整体组成模型和蛋白语言模型表现更好，三类模型组合后性能最高。作者指出，TCR CDR3 聚类表现弱，可能与 HLA 基因型影响 TCR 识别有关；如果不纳入 HLA 信息，跨个体寻找公共 TCR 模式会更困难。

图 2C 显示每个疾病类别的一对其余类别 AUROC：健康/背景 0.97，狼疮 0.98，1 型糖尿病 0.99，COVID-19 0.99，HIV 0.99，流感疫苗 1.00。图 2D 显示正确分类样本的前两类预测概率差异更大，错误分类样本的前两类概率更接近，说明部分错误来自模型本身的不确定性，而不是完全随机失败。

图 2E 是一个重要的临床解释点。成人狼疮患者中，被 BCR-only 模型误判为健康者的 SLEDAI 疾病活动评分较低。原文解释为这些患者可能处于治疗后或疾病较静息状态，因此其免疫受体库更接近健康背景。这一结果提示 Mal-ID 可能更敏感于“当前免疫活动状态”，而不是静态诊断身份。

图 2F 进一步把 pan-disease 模型转化为狼疮特异性检测。通过调节阈值，模型可以达到 97% 灵敏度和 86% 特异度，或 84% 灵敏度和 95% 特异度；一个平衡点为 93% 灵敏度和 90% 特异度。作者据此提出，Mal-ID 既可作为多疾病检测，也可派生为单病种诊断模型。但这仍是概念验证，临床阈值需要根据具体应用场景和疾病患病率确定。

#### Limited impact of batch effects on classification

作者随后检验模型是否只是学到了实验批次或数据来源差异。首先，他们用所有内部数据训练 global model，再在外部 COVID-19 与健康 BCR/TCR 队列上测试。外部 BCR 队列中，模型区分 COVID-19 与健康的 AUROC 达到 1.0，但若直接按最高预测概率分配六类标签，准确率只有 69%；经过基于少量外部样本的阈值调校后，剩余外部样本准确率达到 100%。这说明模型排序信号强，但类别阈值受外部数据疾病构成影响。

外部 TCR 队列中，模型 AUROC 为 0.99，直接最高概率分类准确率为 68%，阈值调校后提升到 90%。原文指出，调校前部分 COVID-19 样本被误分为狼疮，主要与模型 2 的 TCR CDR3 聚类表现不佳有关；禁用模型 2 后，未调校准确率达到 89%，AUROC 为 0.97。

作者还在 Adaptive Biotechnologies genomic DNA TCR 数据上重新训练 Mal-ID，用 1365 个样本区分 common variable immunodeficiency、COVID-19、HIV、类风湿关节炎、1 型糖尿病和健康对照。该数据来自不同实验室，批次效应风险更高，但模型仍达到 0.97 AUROC 和 88% 准确率，并能扩展到超过 1.5 亿条序列。这支持 Mal-ID 框架可以迁移到其他测序技术，但前提是需要重新训练和适配。

在内部批次检验中，作者将一个 COVID-19 PBMC 队列和一批健康重复测序样本整体留出。所有留出的 COVID-19 样本和健康样本均被正确分类。健康样本重复测序中，13 名健康供者里有 9 名两个重复样本均正确分类，且预测概率相关性达到 97% 或更高；少数不一致主要和测序深度较低、CDR3 聚类模型无法匹配到预测簇有关。作者还留出一个独立狼疮队列，5 名狼疮患者中 4 名正确分类，2 名健康对照均正确分类。总体上，这些结果削弱了“模型只是批次分类器”的解释。

#### Limited impact of age, sex, and race on classification

作者进一步评估人口学变量是否驱动分类。健康个体 repertoire 中，性别不能被准确预测；祖源有较弱信号，AUROC 为 0.78；年龄也存在一定信号，区分 50 岁及以上个体的 AUROC 为 0.75。儿童样本的 TCR beta V gene 使用尤其不同，在模型有预测时 AUROC 可达 1.0，但由于 45% 样本出现 abstention，整体准确率只有 55%。

疾病队列之间确实存在年龄、性别和祖源差异。原文列出各队列年龄分布：1 型糖尿病中位年龄 14.5 岁，狼疮 18 岁，流感疫苗 26 岁，HIV 31 岁，健康对照 34.5 岁，COVID-19 48 岁。性别方面，狼疮女性比例为 85%，符合狼疮女性高发。HIV 队列中 89% 个体居住在非洲。

只用年龄、性别或祖源预测疾病时，AUROC 分别为 0.68、0.59 和 0.79；三者联合为 0.85，低于 Mal-ID 的 0.98。作者还将年龄、性别、祖源从 ensemble 特征矩阵中回归掉，分类 AUROC 从 0.98 降至 0.96。这说明人口学变量确实有影响，但不能充分解释 Mal-ID 的主要疾病分类性能。

需要注意的是，这一部分只能说明已测量的人口学变量不是主要解释，并不能证明所有未测量混杂都不存在。例如既往感染史、治疗方案、地理暴露、样本来源和疾病严重程度仍可能贡献部分信号。

#### Language model recapitulates immunological knowledge

![图3：模型3根据蛋白语言模型嵌入识别疾病相关 IGHV 基因和同种型](../../assets/immunology/2025-disease-diagnostics-immune-receptor-sequences/fig3-ighv-isotype-shap.png)

图 3 是整篇文章最关键的可解释性结果之一。作者使用模型 3 的 SHAP 值评估不同 IGHV 基因和同种型组合对疾病预测的贡献。结果显示，模型优先使用的 V gene 和同种型与既往免疫学知识相符。

COVID-19 预测中，IGHV1-24 和 IGHV2-70 被优先使用，且 IgG 信号突出。这符合 SARS-CoV-2 特异性 B 细胞常见 IgG 表达的文献认识。HIV 预测中，IGHV1-2 和 IGHV4-34 具有较高权重，并且 mutated IgM/D 信号更明显。流感疫苗预测中，IGHV3-23 以及 IgG、mutated IgM/D 信号较重要。狼疮中，IGHV4-34 和 IGHV4-59 权重较高，IgA 也具有信息量；这与狼疮相关 IgA 自身抗体文献相吻合。1 型糖尿病中，IgA 和其他同种型均有贡献。

作者还检验了是否仅凭同种型比例就能预测疾病。单独使用 isotype proportion、不使用序列信息时，AUROC 只有 0.68，明显低于 Mal-ID 的 0.98 以上。这一点说明模型并非只是利用不同疾病样本中 IgG/IgA/IgM 比例差异，而是在同种型内部进一步利用序列特征。

这个结果的科学意义在于，模型不是完全不可解释的黑箱。它至少部分恢复了已知抗原特异性或疾病相关 BCR 使用模式，也提出一些尚未被单病种文献充分描述的 V gene 候选信号。需要谨慎的是，SHAP 表示模型预测贡献，不等于证明这些 V gene 在疾病中具有因果作用。

![图4：模型2和模型3对已知 SARS-CoV-2 结合抗体序列的识别](../../assets/immunology/2025-disease-diagnostics-immune-receptor-sequences/fig4-known-sars-cov-2-binders.png)

作者进一步测试一个关键问题：模型是否真的学到疾病相关抗原特异性序列模式。为此，他们使用外部 CoV-AbDab 数据库中的 SARS-CoV-2 结合 BCR heavy chain 序列，并与健康供者序列比较。重要的是，这些外部 binder 序列没有用于训练。

图 4A-D 显示模型 2 的 CDR3 聚类可以识别一部分已知 binder，但召回率低。若只要求相同 IGHV、IGHJ 和 CDR3 长度，模型 2 可以找到部分 SARS-CoV-2 cluster 匹配；若再加上 85% CDR3 序列一致性约束，精确度可以很高，但召回进一步降低。这符合模型 2 的本质：它保守、可解释，但只能捕捉高度相似的公共或收敛序列。

图 4E-I 显示模型 3 的语言模型嵌入能把已知 SARS-CoV-2 binder 排在比健康序列更高的 COVID-19 关联概率位置。按 IGHV 基因分层，AUROC 最高可达 0.78，AUPRC 相对基线最高可提高 6.9 倍。模型 3 相比模型 2 通常有更高召回，但也带来更多假阳性。这是合理的：语言模型试图捕捉更宽松的功能相似性，而不是只找近似相同序列。

作者还对流感已知 binder 做了类似验证，发现模型 2 和模型 3 在关键 IGHV 基因中也能优先排序 binding sequences，但信号弱于 COVID-19，最高 AUROC 为 0.65，AUPRC 相对基线最高提升 4.0 倍。作者认为这可能因为流感已知抗体数据库来自不同年份、不同感染或接种背景，而训练数据来自特定年度流感疫苗后样本。

TCR 的 SARS-CoV-2 binder 验证更弱。模型 2 表现差，模型 3 对已知 SARS-CoV-2 特异性 TCR 的富集也较弱，TRBV 基因内最高 AUROC 只有 0.56，AUPRC 最高相对基线提升 1.30 倍。作者提出原因包括 TCR 识别依赖 HLA 分子、不同队列 HLA 背景差异、体外刺激可能激活旁观者克隆、TCR 分析没有排除 naive T cells 等。

这一结果非常重要：Mal-ID 的患者级诊断表现很强，但单条抗原特异性 TCR 识别并不强。这说明模型的患者分类信号可能不仅来自直接结合抗原的 receptor，也可能来自更广泛的疾病相关免疫状态改变。

### 原文讨论中的主要结论

作者在讨论中强调，Mal-ID 的性能来自三类互补信号：整体 repertoire composition、重要序列群的检测、以及语言模型对单条 receptor 序列的表示。BCR 和 TCR 联合优于单独使用任一数据类型，说明不同疾病对 B 细胞和 T 细胞反应的依赖不同。比如 1 型糖尿病通常被认为以 T 细胞介导为主，TCR-only 模型确实比 BCR-only 更能区分 T1D，但两者联合仍进一步提高性能。狼疮既有自身抗体又有 T 细胞参与，因此 BCR 与 TCR 都有信息，联合效果最好。

作者还指出，多疾病建模比单一疾病对健康对照更有意义。单病种 versus 健康很容易识别一般炎症或疾病严重程度；多疾病模型更有机会识别某一疾病相对于其他免疫状态的特异性模式。但临床转化仍需要确定不同疾病和不同场景下可接受的灵敏度、特异度、阈值和疾病患病率。

作者明确提出未来需要解决的问题：同一患者可能有多个疾病或合并症；同一疾病存在严重程度和亚型；组织活检等非外周血样本可能提供额外信息；模型还需要面对训练集中不存在的新疾病，例如未来大流行病。这些问题都说明当前 Mal-ID 仍是概念验证，不是直接可用的全场景临床诊断系统。

### 作者结论与证据强度

作者已经较有力证明：在这组经过整理的队列中，BCR/TCR repertoire 序列包含足够强的疾病状态信号，可以区分六类感染、自身免疫、疫苗反应和健康状态；BCR 与 TCR 联合优于单一模态；三类模型组合优于多数单组件；模型识别的部分 V gene、同种型和外部 SARS-CoV-2 binder 信号符合已知免疫学。

作者合理但尚未完全证明的推断是：该框架未来可发展为临床多疾病检测或单病种诊断工具。现有证据支持“有潜力”，但还不足以支持广泛临床替代。真实临床需要前瞻性队列、真实鉴别诊断场景、合并症、多标签疾病、近期感染和疫苗史、治疗状态、样本量和测序深度优化。

作者没有证明的是：模型学到的全部信号都是抗原特异性 receptor。尤其 TCR binder 验证较弱，说明 patient-level 分类信号可能包括旁观者激活、免疫组成改变、疾病活动度、治疗状态、样本时间点和其他免疫背景。

## 独立方法学详解

这篇文章的方法学可以拆成五层：样本与测序、序列预处理、三类基础模型、集成模型、稳健性验证。

### 样本与测序

样本与测序层面，作者从外周血 RNA 中扩增 TCR beta chain 和不同 IgH 同种型，采用 Illumina MiSeq paired-end 测序。BCR 只保留 class-switched IgG/IgA，以及具有至少 1% SHM 的 IgD/IgM，以尽量排除 naive B cells；TCR 不存在体细胞高突变。VDJ 注释使用 IgBLAST v1.3.0，只保留 productive rearrangements，并对低质量 V gene 匹配进行过滤。

### 序列预处理与 clonal lineage 压缩

序列预处理层面，作者在同一个体内按 V gene、J gene、CDR3 长度和序列相似性进行单链接聚类，以推断 clonal lineages。BCR 使用较宽松的 CDR-H3 相似性阈值以容纳 SHM，TCR 使用 CDR3b 相似性阈值。随后每个 clone 每个同种型保留 read 数最高的代表序列。这个步骤的目的不是寻找疾病模式，而是减少同一克隆内重复序列对模型的影响。

### 模型 1：repertoire composition classifier

模型 1 是 repertoire composition classifier。它把每个样本的 V/J gene usage 转成计数特征，并按样本总 clone 数归一化，再进行 log 转换、Z-score 标准化和 PCA 降维。BCR 额外加入每个同种型的 SHM 中位数和 SHM 比例。最终 BCR composition 模型包含 IgG、IgA、IgM/D 三组特征，TCR composition 模型包含 TRB 的 V/J 使用特征，并用 logistic regression 预测疾病类别。

### 模型 2：CDR3 convergent clustering classifier

模型 2 是 CDR3 convergent clustering classifier。作者在 train-1 数据中按相同 V gene、J gene 和 CDR3 长度寻找高度相似的 CDR3 cluster，再用 Fisher 精确检验筛选在某一疾病中富集的 cluster。新样本被映射到这些疾病富集 cluster，cluster 命中数形成特征，再用 logistic regression 预测疾病。如果一个样本没有任何序列落入预测 cluster，模型 2 会 abstain。这个 abstention 机制解释了为什么模型 2 的 AUROC 和 accuracy 需要分开看。

### 模型 3：language model embedding classifier

模型 3 是 language model embedding classifier。作者使用 30 层、1.5 亿参数的 ESM-2，将 CDR-H3/CDR3b 序列嵌入为 640 维向量。第一阶段在每个 IGHV+isotype 或 TRBV 类别内训练 sequence-level disease classifier；第二阶段把同一患者样本内的序列预测概率按 V gene/isotype 或 TRBV 聚合，再训练 patient-level model。由于单条序列真实抗原特异性未知，sequence-level label 是患者疾病标签，因此这是弱监督学习。作者用 SHAP 解释第二阶段模型中不同 IGHV/isotype 或 TRBV 特征对疾病预测的贡献。

### 统计学分析方法

Mal-ID 的统计学核心是严格区分“序列级别样本很多”和“真正独立的个体数量有限”。因此所有训练、验证和测试划分都按个体进行，而不是按序列进行。同一个人的序列高度相关，如果把序列随机拆到训练集和测试集，会造成数据泄漏并高估性能。这里的独立分析单位是 patient/sample，序列只是构成患者级特征的原始观测。

模型性能主要用 AUROC、AUPRC、accuracy、sensitivity 和 specificity 描述。AUROC 衡量模型对阳性和阴性样本的排序能力，适合比较不同疾病类别的一对其余任务；AUPRC 更受阳性类别比例影响，适合评估已知 binder 富集这种不平衡任务；accuracy 是最高概率分类后的正确比例，但在类别不均衡或阈值未校准时不如 AUROC 稳定。灵敏度和特异度用于临床阈值解释，必须结合具体场景选择，不能只追求总体准确率。

模型 2 的疾病富集 CDR3 cluster 使用 Fisher exact test。输入是某个 cluster 是否出现在某疾病个体与其他个体中，回答的是该 cluster 是否在某疾病中富集。Fisher 检验适合稀疏列联表，但在大量 cluster 上反复检验会产生多重比较问题，因此需要训练集内筛选、验证集调参和独立测试集评估来控制过拟合。

模型 3 是弱监督学习，单条 receptor 继承患者疾病标签。这个标签策略统计上有噪声，因为一个患者的大多数 BCR/TCR 序列未必与疾病直接相关。作者通过按 V gene/isotype 或 TRBV 分层训练、再聚合到患者级模型，试图从大量噪声序列中提取稳定的疾病信号。解释时必须记住：sequence-level 高分表示模型认为这条序列有疾病相关模式，不等于它已经被证明是抗原特异性 receptor。

SHAP 用于解释模型 3 的 patient-level 特征贡献。输入是不同 IGHV/isotype 或 TRBV 分组聚合后的模型输出，结果是这些特征对疾病预测概率的边际贡献。SHAP 可以帮助发现模型使用的免疫学线索，例如 IGHV4-34 与狼疮，但它解释的是预测模型行为，不证明 V gene 或同种型对疾病有因果作用。

人口学和批次混杂通过多种方式评估：demographics-only classifier 测试年龄、性别和祖源本身能否预测疾病；残差化分析把人口学变量从 ensemble 特征中回归掉，再观察 AUROC 是否明显下降；外部队列和批次留出用于测试模型是否依赖实验来源。残差化后性能从 0.98 降到 0.96，说明人口学有贡献但不是全部信号；不过未测量混杂，例如治疗、近期感染、地理暴露和疾病活动度，仍不能完全排除。

### 集成模型和数据泄漏控制

集成模型层面，作者把三类 BCR 模型和三类 TCR 模型的预测概率拼接起来，用 ridge logistic regression 作为 metamodel。训练过程在每个 cross-validation fold 内独立完成，并且保持 train、validation、test 的个体级隔离。对于 multi-stage 模型，sequence-level 和 patient-level 阶段又进一步使用 train-1 和 train-2 分离，避免同一层数据同时参与特征发现和最终评估。

### 稳健性验证和混杂控制

稳健性验证层面，作者做了四类检查：第一，外部 cDNA BCR/TCR COVID-19 队列验证；第二，Adaptive Biotechnologies genomic DNA TCR 数据上的重新训练；第三，内部批次留出和重复测序样本一致性检验；第四，年龄、性别、祖源预测、demographics-only disease classifier 和人口学残差化分析。这些步骤共同服务于一个目的：判断模型是否主要学习疾病相关 repertoire signal，而不是批次、人口学或数据来源。

## 生物学与临床意义

这篇文章最重要的生物学意义是：疾病可以通过分布式方式改变 adaptive immune repertoire，而不只是留下少数可直接识别的抗原特异性克隆。感染可能产生抗原特异性 B 细胞扩增；自身免疫病可能形成慢性自身反应和 T-B 协同异常；疫苗接种在特定时间窗会提高血液中反应性浆母细胞或相关克隆频率。Mal-ID 试图把这些不同层级的免疫改变统一为可计算表型。

临床上，最值得注意的是模型可能更接近“免疫状态读数”而非“终身诊断标签”。狼疮低活动患者被判为健康的结果说明，模型可能对当前疾病活动、治疗后免疫静息状态或外周血免疫扰动更敏感。若目标是初诊筛查，这可能造成漏诊；若目标是监测病情活动或治疗反应，则可能成为优势。

因此，未来临床应用必须先定义问题：是诊断是否患病，还是判断当前免疫活动，还是预测复发、进展或治疗反应。不同目标需要不同队列、标签、随访和阈值。

## 局限性与危险假设

最大的危险假设是把“疾病分类准确”直接等同于“模型识别了疾病特异性抗原受体”。原文结果并不支持这种强解释。BCR 层面的 SARS-CoV-2 binder 验证提供了支持，但 TCR 层面较弱；而患者级分类信号强，说明模型可能利用了更广泛的免疫状态。

第二个危险假设是训练集疾病类别足以代表真实临床世界。现实患者可能刚接种疫苗、近期感染、合并自身免疫、使用免疫抑制剂、存在肿瘤或处于慢性炎症状态。若模型只能在已知类别中强制选择，就可能把未知免疫状态错误映射到某个已知疾病。

第三个危险假设是外周血足以代表所有疾病相关免疫过程。对于组织局部免疫病变、肿瘤微环境或黏膜免疫，外周血 repertoire 可能只是部分反映。未来需要比较外周血、组织、局部淋巴结构和空间免疫生态。

## 深度研究洞察

这篇文章实际上把 BCR/TCR repertoire 定义成一种介于基因组、环境暴露和疾病表型之间的动态中间表型。它不同于 germline genetics，因为 receptor repertoire 会随感染、疫苗、治疗和自身免疫活动变化；它也不同于普通血液标志物，因为它不是一个浓度，而是由数百万条选择过的序列构成的群体结构。这个群体结构同时携带疾病信号和患者免疫史，因此信息量大，也更容易混杂。

最值得借鉴的是模型架构与生物层级一致。作者没有把所有序列压成一个黑箱向量，而是保留 BCR/TCR、V gene、isotype、CDR3、sequence embedding、patient-level aggregation 等层级。这种设计让模型解释和生物学验证成为可能。对于多组学、空间组学和肿瘤微环境研究，这个原则非常重要：模型结构应该尽量尊重生物组织层级，而不是只追求端到端预测。

这篇文章也提醒我们，未来真正有价值的可能不是横断面诊断，而是纵向免疫轨迹。若 repertoire 能读出当前免疫状态，那么更强的问题是：它能否预测感染后恢复、自身免疫复发、癌前病变进展、疫苗反应持续时间或治疗获益。静态分类只是第一步，动态转归预测才更接近精准医学。

## 可借鉴或迁移的思路

这篇文章与胃癌、GIMs 和 H. pylori 不是直接同一领域，但在研究范式上高度相关。H. pylori 感染到慢性胃炎、萎缩、肠化、异型增生和胃癌，是长期宿主-微生物-免疫-组织重塑过程。传统风险模型多依赖流行病学变量、血清学、病理分级、遗传风险和内镜结果，但未必能完整反映宿主长期免疫选择。

可借鉴的问题是：外周或胃黏膜局部 BCR/TCR repertoire 能否区分 H. pylori 感染、根除后状态、慢性萎缩性胃炎、肠化、异型增生和早期胃癌？更进一步，repertoire 是否能预测 GIM 进展或根除后逆转？如果要做这类研究，设计必须纵向、必须以病理和内镜为锚点、必须控制地区、年龄、H. pylori 暴露史、治疗史和测序批次，否则模型很容易学到队列差异而非进展生物学。

这篇文章还可与因果稳定学习结合。Mal-ID 主要通过残差化和外部验证排除已知混杂。对于胃癌预防研究，可以进一步追问：哪些 immune repertoire 或多组学特征在不同医院、不同地区、不同 H. pylori 流行背景和不同筛查策略下仍稳定预测 GIM 进展？这比单队列高 AUROC 更接近真实世界转化。

如果与空间转录组结合，外周 BCR/TCR 可以作为系统免疫记忆读数，胃黏膜空间组学可以作为局部免疫生态读数，宿主遗传可以作为上游调控层。三者整合可能形成一种“系统免疫记忆 + 局部组织生态 + 遗传调控”的胃癌精准预防框架。

## 可复用学术表达

这篇文章值得学习的一种表达方式，是把检测对象上升为“机体自身记录”。作者不是说“我们测了 BCR/TCR”，而是强调临床诊断很少使用 adaptive immune system 自身记录的抗原暴露信息。这种写法能把技术方法转化为科学问题。

第二种表达方式，是按生物层级描述模型，而不是按算法名称堆砌。整体组成、CDR3 聚类、语言模型嵌入分别对应不同免疫信号尺度。未来写多组学或空间组学方法时，也应优先解释每个模型组件对应什么生物层级。

第三种表达方式，是主动区分分类性能和临床应用。原文反复强调阈值、灵敏度、特异度和疾病患病率依赖具体场景。这种写法比单纯强调 AUROC 更严谨，也更像高水平转化医学论文。

## 相关论文与概念

Roskin 等关于 HIV BCR repertoire selection 的研究与本文直接相关，因为本文 HIV 数据和 BCR 选择逻辑部分继承了该方向。它说明慢性感染可以在 BCR repertoire 中留下可检测的选择模式。

Emerson 等关于 TCR immunosequencing 识别 CMV 暴露史的研究是重要前身。它证明公共 TCR 模式可反映既往抗原暴露，但本文也显示 exact sequence matching 对多疾病诊断过于狭窄。

Bashford-Rogers 等关于多种 immune-mediated diseases 的 BCR repertoire 分析提供了自身免疫病背景。该类研究把 BCR repertoire 从抗体发现工具扩展为疾病状态比较工具。

DeepTCR、免疫受体 autoencoder 和 antibody language model 相关工作是方法学比较对象。它们关注序列表示学习，而本文的特点是将序列表示放入 BCR/TCR 双模态、多层级、患者级诊断框架中。

开放集识别、多标签分类、概率校准和不确定性估计是 Mal-ID 后续临床化必须引入的概念。没有这些机制，模型会把未知或混合免疫状态强制分配到已知疾病类别。
