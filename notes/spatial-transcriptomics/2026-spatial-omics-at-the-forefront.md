# Spatial omics at the forefront: emerging technologies, analytical innovations, and clinical applications

## 本文目录

- [基本信息](#基本信息)
- [本论文主图](#本论文主图)
- [生物学故事前情](#生物学故事前情)
- [重要缩写表](#重要缩写表)
- [论文详细解读](#论文详细解读)
- [研究问题与科学背景](#研究问题与科学背景)
- [研究设计与数据结构](#研究设计与数据结构)
- [方法与分析框架](#方法与分析框架)
- [原文结果完整梳理](#原文结果完整梳理)
  - [Recent advances in spatial omics technologies](#recent-advances-in-spatial-omics-technologies)
  - [Analytical breakthroughs in tumor spatial profiling](#analytical-breakthroughs-in-tumor-spatial-profiling)
  - [Unraveling tumor microenvironment complexity](#unraveling-tumor-microenvironment-complexity)
  - [Clinical and translational applications of spatial omics](#clinical-and-translational-applications-of-spatial-omics)
  - [Conclusions and future directions](#conclusions-and-future-directions)
- [作者结论与证据强度](#作者结论与证据强度)
- [独立方法学详解](#独立方法学详解)
  - [综述型文章的证据结构](#综述型文章的证据结构)
  - [空间组学平台选择方法](#空间组学平台选择方法)
  - [空间数据处理流程](#空间数据处理流程)
  - [统计学分析方法](#统计学分析方法)
  - [空间计算模型和多模态整合](#空间计算模型和多模态整合)
  - [临床转化研究设计](#临床转化研究设计)
  - [可重复性资源和迁移注意点](#可重复性资源和迁移注意点)
- [生物学与临床意义](#生物学与临床意义)
- [局限性与危险假设](#局限性与危险假设)
- [深度研究洞察](#深度研究洞察)
- [可借鉴或迁移的思路](#可借鉴或迁移的思路)
- [可复用学术表达](#可复用学术表达)
- [相关论文与概念](#相关论文与概念)

## 基本信息

- 原文题名：Spatial omics at the forefront: emerging technologies, analytical innovations, and clinical applications
- 期刊：Cancer Cell 44, 24-49
- 年份：2026
- DOI：10.1016/j.ccell.2025.12.009
- 作者：Yunhe Liu、Yibo Dai、Linghua Wang
- 通讯作者：Linghua Wang
- 研究领域：空间组学、肿瘤微环境、空间转录组、空间蛋白组、空间代谢组、多模态整合、精准肿瘤学
- 关键词：spatial omics、spatial transcriptomics、spatial proteomics、spatial metabolomics、tumor microenvironment、multimodal integration、clinical translation、precision oncology
- PDF 归档：`pdfs/processed/cancer-cell-spatial-omics-review-2026.pdf`
- PDF 解析质量：正文、图题、图注、表格标题、参考文献和主要章节均可解析；Table 1 内容跨页较密，本文以截图和概括性解读为主，不逐项重排完整表格。
- 图像截取说明：已截取主文 Fig. 1-5 和 Table 1 两页截图，图像位于 `assets/spatial-transcriptomics/2026-spatial-omics-review/`。

## 本论文主图

| 原文图表 | 原文图题/核心信息 | 是否截取 | 图像文件 | 放置位置 |
|---|---|---|---|---|
| Fig. 1 | Overview of spatial omics technologies：空间转录组、蛋白组、代谢组、多组学和 3D/4D profiling 技术全景 | 是 | `assets/spatial-transcriptomics/2026-spatial-omics-review/fig1-overview-spatial-omics-technologies.png` | [Recent advances in spatial omics technologies](#recent-advances-in-spatial-omics-technologies) |
| Table 1 | Comparison of major commercial high-resolution spatial transcriptomic profiling platforms：高分辨率商业空间转录组平台比较 | 是 | `assets/spatial-transcriptomics/2026-spatial-omics-review/table1-commercial-spatial-transcriptomics-platforms-p1.png`; `table1-commercial-spatial-transcriptomics-platforms-p2.png` | [Recent advances in spatial omics technologies](#recent-advances-in-spatial-omics-technologies) |
| Fig. 2 | Computational tools and analytical frameworks for spatial omics：空间组学数据处理、单细胞/亚细胞分析、空间组织、进化、多模态整合和 3D 重建 | 是 | `assets/spatial-transcriptomics/2026-spatial-omics-review/fig2-computational-tools-frameworks.png` | [Analytical breakthroughs in tumor spatial profiling](#analytical-breakthroughs-in-tumor-spatial-profiling) |
| Fig. 3 | Spatial mapping of TME niches：肿瘤微环境中九类重要空间 niche | 是 | `assets/spatial-transcriptomics/2026-spatial-omics-review/fig3-spatial-mapping-tme-niches.png` | [Unraveling tumor microenvironment complexity](#unraveling-tumor-microenvironment-complexity) |
| Fig. 4 | Hierarchy of spatial archetypes across scales：从细胞、niche、community 到 whole-tumor ecosystem 的空间层级 | 是 | `assets/spatial-transcriptomics/2026-spatial-omics-review/fig4-spatial-archetypes-hierarchy.png` | [Unraveling tumor microenvironment complexity](#unraveling-tumor-microenvironment-complexity) |
| Fig. 5 | From spatial insights to clinical impact：空间组学从临床场景、研究设计、空间洞察到临床部署的路线图 | 是 | `assets/spatial-transcriptomics/2026-spatial-omics-review/fig5-spatial-insights-clinical-impact.png` | [Clinical and translational applications of spatial omics](#clinical-and-translational-applications-of-spatial-omics) |

## 生物学故事前情

癌症不是一团均质细胞，而是由肿瘤克隆、免疫细胞、成纤维细胞、血管、神经、微生物和细胞外基质共同构成的组织生态系统。单细胞测序解决了“有哪些细胞状态”的问题，却经常丢失这些细胞在组织中如何排列、谁和谁相邻、哪些细胞群形成免疫抑制或免疫激活结构、肿瘤克隆如何沿空间边界扩展等信息。

空间组学出现之前，病理学能看见组织结构，但分子维度有限；bulk 多组学能测分子，但混合了不同细胞和区域；单细胞测序能拆细胞状态，但缺空间坐标。肿瘤学真正需要的是把“形态、位置、分子、细胞互作和临床结局”放到同一个坐标系里。空间组学正是为了补上这个断层。

这篇综述的前情是：空间技术已经从少数研究型平台扩展到商业化空间转录组、空间蛋白组、空间代谢组、多模态和 3D/4D 成像；计算方法也从简单细胞注释发展到空间 niche、community、生态系统、空间 foundation model 和临床可部署 assay。作者要讲的不是某一个实验结果，而是整个领域如何从“能在组织上测分子”走向“用空间读数解释肿瘤演化、治疗反应和精准肿瘤学决策”。

## 重要缩写表

| 缩写 | 中文含义 | 本文语境中的具体指代 | 阅读时注意 |
|---|---|---|---|
| ST | 空间转录组 | 保留组织空间坐标的 RNA profiling 技术总称 | 不同平台的分辨率、通量和 FFPE 兼容性差异很大 |
| TME | 肿瘤微环境 | 肿瘤细胞周围免疫、基质、血管、神经、微生物等生态成分 | TME 不是单一细胞类型，而是空间组织系统 |
| NGS | next-generation sequencing | 基于测序读出空间条形码或 transcript 的技术路线 | 高通量不等于高空间分辨率 |
| FFPE | 福尔马林固定石蜡包埋 | 临床病理样本最常见保存形式 | 适合回顾性队列，但 RNA 质量和平台选择受限 |
| FISH | 荧光原位杂交 | 成像型空间转录组的基础技术逻辑 | 目标基因 panel 选择会限制发现范围 |
| IMC | imaging mass cytometry | 金属标记抗体结合质谱成像的空间蛋白组技术 | 蛋白 panel 通常低于转录组，但蛋白更接近功能状态 |
| CODEX | co-detection by indexing | 循环荧光抗体成像平台 | 适合高维蛋白空间定位，依赖抗体质量 |
| MALDI-MSI | 基质辅助激光解吸电离质谱成像 | 空间代谢组/脂质组常用技术 | 分子注释和空间分辨率是关键限制 |
| CNV | 拷贝数变异 | 可从空间表达或基因组信号中推断肿瘤克隆结构 | 表达推断 CNV 只是近似，不等同于 DNA 测序 |
| TLS | 三级淋巴结构 | 肿瘤内 B/T 细胞组织化免疫结构 | TLS 的位置、成熟度和癌种背景影响临床意义 |
| MRD | 微小残留病灶 | 治疗后未被常规检测发现但可能导致复发的残留肿瘤 | 空间读数可帮助解释 MRD 生态位，不一定直接替代 ctDNA |
| TMA | tissue microarray | 组织芯片 | 适合高通量验证，但取样区域有限 |
| MIS | minimally invasive surgery | 微创手术 | Fig. 5 中作为临床取样场景之一 |
| AI | 人工智能 | 用于图像、空间组学和临床决策整合的模型 | 需要标准化数据和可解释临床验证 |

## 论文详细解读

### 研究问题与科学背景

这篇综述的核心问题是：空间组学怎样把肿瘤研究从“细胞类型清单”推进到“组织生态系统机制图谱”，并最终进入临床研究和精准肿瘤学。作者从三个层面展开：第一，空间组学平台本身如何演进；第二，空间数据分析如何从细胞注释走向 niche、community、生态系统和多模态整合；第三，空间读数如何服务于癌前病变、转移、MRD、治疗反应、 biomarker 和 target discovery。

文章把空间组学定义为下一代预测和精准肿瘤学的基础设施之一。它的意义不只是“保留坐标”，而是用坐标把肿瘤克隆、免疫反应、基质结构、微生物、神经接口、代谢状态和治疗压力连接起来。相比单细胞 RNA-seq，空间组学最关键的新增信息是细胞邻近关系、区域结构和组织层级。

### 研究设计与数据结构

本文是综述，不是原始实验研究，没有单一 cohort、纳排标准或统计分析队列。作者整合了空间转录组、空间蛋白组、空间代谢组、多模态空间组学、3D/4D profiling、空间计算方法和肿瘤临床转化研究的代表性文献。

从结构上看，文章按“技术平台 -> 计算分析 -> 肿瘤生态机制 -> 临床转化”的路径组织。Fig. 1 和 Table 1 负责平台层；Fig. 2 负责计算框架；Fig. 3 和 Fig. 4 负责肿瘤微环境和空间生态层级；Fig. 5 负责临床转化设计。这个结构本身就是作者的论证：空间组学要进入临床，不能只靠单个平台或单个算法，必须同时解决样本、技术、分析、验证和部署问题。

### 方法与分析框架

这篇文章的方法框架不是实验流程，而是综述式的技术-分析-转化框架。技术层面，作者把空间组学分为 transcriptomics、proteomics、metabolomics、multi-omics 和 3D/4D profiling；其中空间转录组又分为 imaging-based 和 sequencing-based，前者包括 cyclic decoding 和 cyclic in situ sequencing，后者包括 barcode-to-cell 和 tissue-on-array capture。

计算层面，作者把空间分析拆成数据处理、数据增强、单细胞/亚细胞分析、空间细胞互作、空间 niche/community、肿瘤克隆演化、多模态整合和 3D 重建。临床层面，作者强调 study design 必须从临床问题和 endpoint 出发，再反推样本类型、保存方式、平台选择、空间分辨率、分析框架和验证策略。

### 原文结果完整梳理

#### Recent advances in spatial omics technologies

![图1：空间组学技术全景](../../assets/spatial-transcriptomics/2026-spatial-omics-review/fig1-overview-spatial-omics-technologies.png)

中文图注（基于原文图注）：Fig. 1 总结空间组学技术类型。A：空间转录组分为 in situ imaging-based 和 spatial barcoding sequencing-based。成像型方法又包括 cyclic combinatorial decoding 和 cyclic in situ sequencing，区别在于通过荧光编码还是碱基读取识别目标；测序型方法包括 barcode-to-cell delivery 后进行单细胞/单核测序，以及 tissue-on-array 的空间条形码捕获和 NGS。B：空间蛋白组包括多重荧光抗体成像和金属标记抗体质谱成像等。C：空间代谢组通过激光、离子束、电喷雾或质谱成像测量组织中的小分子、脂质和代谢物。D：空间多组学可同时或连续测量 DNA/RNA/蛋白/组织形态等信号。E：3D/4D profiling 通过连续切片、组织透明化或时间轴数据重建空间结构。

作者首先梳理平台层的变化。空间转录组不再只是早期低分辨率 capture array，而是形成了高分辨率 imaging-based 和 sequencing-based 两大路线。成像型方法的优势是单细胞或亚细胞分辨率、形态保留和 FFPE 兼容性较强；限制是 panel 需要预设，通量和循环次数有成本。测序型方法的优势是更接近全转录组或高通量发现；限制是分辨率、捕获效率和单细胞边界解析依赖平台。

![表1-1：高分辨率空间转录组商业平台比较第一页](../../assets/spatial-transcriptomics/2026-spatial-omics-review/table1-commercial-spatial-transcriptomics-platforms-p1.png)

![表1-2：高分辨率空间转录组商业平台比较第二页](../../assets/spatial-transcriptomics/2026-spatial-omics-review/table1-commercial-spatial-transcriptomics-platforms-p2.png)

中文图注（基于原文表格）：Table 1 比较主要商业高分辨率空间转录组平台，包括 imaging-based、in situ sequencing、tissue-on-array capture 和 barcode-to-cell 等类别。表格重点比较平台机制、分辨率、基因通量、组织兼容性、样本类型、读出方式和应用场景。该表不是性能排名，而是平台选择矩阵：不同研究问题需要在分辨率、capture area、whole-transcriptome 能力、FFPE 兼容性、成本和多组学扩展之间取舍。

空间蛋白组和代谢组补充了 RNA 无法直接代表功能状态的问题。蛋白组能更接近受体、配体、免疫检查点和磷酸化等功能层；代谢组能读出局部营养、脂质、药物分布和代谢微环境。空间多组学进一步把 DNA/RNA/蛋白/形态或 TCR/BCR 信息连接起来，但也带来配准、批次、模态尺度和组织消耗的困难。

#### Analytical breakthroughs in tumor spatial profiling

![图2：空间组学计算工具和分析框架](../../assets/spatial-transcriptomics/2026-spatial-omics-review/fig2-computational-tools-frameworks.png)

中文图注（基于原文图注）：Fig. 2 展示空间组学分析框架。A：数据处理包括细胞分割、归一化、harmonization、分辨率增强和特征增强。B：单细胞/亚细胞分析包括空间单位定义、mRNA 亚细胞定位和空间细胞互作推断。C：空间组织和生态系统分析包括 context-aware clustering、从细胞到 niche/community/ecosystem 的层级建模。D：空间解析肿瘤演化。E：多模态整合和 3D 体积模型重建。

作者将空间计算的第一步定义为数据处理和增强。对于成像型平台，细胞分割决定了转录本或蛋白信号归属到哪个细胞；对于 spot/bin 型平台，数据需要 deconvolution、resolution enhancement 或 cell reconstruction。归一化、批次校正和跨平台 harmonization 是后续比较的前提，否则空间差异很容易混入技术差异。

第二层是空间单位的定义。空间单位可以是 spot、cell、subcellular compartment、niche、community 或 whole-tumor region。不同单位回答不同问题：亚细胞定位回答 RNA 或蛋白在细胞内何处富集；细胞邻近关系回答谁和谁互动；niche/community 回答多细胞结构如何组织；ecosystem 回答整个肿瘤空间结构和临床结局如何相关。

第三层是多模态和 3D。空间转录组、蛋白组、代谢组、病理图像和基因组变异需要共同配准到组织结构上。作者特别强调 multimodal integration 和 spatial foundation models，因为未来临床部署很可能不是单一 marker，而是组织形态、空间细胞生态和分子特征共同构成的风险模型。

#### Unraveling tumor microenvironment complexity

![图3：肿瘤微环境空间 niche](../../assets/spatial-transcriptomics/2026-spatial-omics-review/fig3-spatial-mapping-tme-niches.png)

中文图注（基于原文图注）：Fig. 3 示意肿瘤微环境中九类重要空间 niche 的细胞组成和组织方式。图中强调 TLS、肿瘤-基质边界、免疫抑制区、血管/缺氧相关 niche、神经接口、微生物相关区域等结构如何通过空间组织影响肿瘤生物学和临床结局。

作者把空间组学对 TME 的贡献概括为：它不仅识别细胞类型，还识别细胞如何组织成功能结构。TLS 是最典型例子，它不是“有 B 细胞和 T 细胞”这么简单，而是局部抗原呈递、B 细胞成熟、T cell help 和抗肿瘤免疫被组织起来的结构。不同癌种中 TLS 的位置、成熟状态和免疫细胞组成会影响预后和免疫治疗反应。

空间组学也揭示肿瘤-基质边界、CAF niche、髓系免疫抑制区、血管周围结构、缺氧区域、微生物生态位和神经-肿瘤接口。这些结构用 dissociated single-cell sequencing 很难完整恢复，因为一旦消化组织，邻近关系和区域边界就丢失了。

![图4：跨尺度空间 archetype 层级](../../assets/spatial-transcriptomics/2026-spatial-omics-review/fig4-spatial-archetypes-hierarchy.png)

中文图注（基于原文图注）：Fig. 4 展示空间 archetype 的层级结构：从 individual cells 到 multicellular niches，再到 spatial communities 和 whole-tumor ecosystems。该图强调空间结构不是单一尺度现象，而是由细胞邻近、功能 niche、多区域组织和整个肿瘤生态共同构成。

Fig. 4 是全篇概念核心。作者提出 spatial archetypes across scales，意思是空间模式应按层级理解。单个细胞状态很重要，但许多临床相关现象发生在多细胞 niche 或 whole-tumor ecosystem 层面。例如免疫治疗反应可能取决于肿瘤细胞、抗原呈递细胞、T 细胞和 CAF 是否形成有利的接触结构；转移适应可能取决于某个器官微环境中肿瘤克隆、基质和免疫屏障的组合。

#### Clinical and translational applications of spatial omics

![图5：从空间洞察到临床影响](../../assets/spatial-transcriptomics/2026-spatial-omics-review/fig5-spatial-insights-clinical-impact.png)

中文图注（基于原文图注）：Fig. 5 展示空间组学临床转化路线。A：空间 profiling 可用于早期肿瘤发生、转移、MRD 和治疗反应等临床场景。B：临床转化设计包括纵向采样、横断面多部位采样、样本类型和保存方式选择。C：空间数据可揭示肿瘤演化、MRD 预测、细胞组织和 niche、细胞互作与信号 hub。D：从发现到部署包括药物靶点空间分布、肿瘤克隆演化和治疗反应、TME 调控、细胞治疗追踪、target discovery、biomarker 转化、癌前到浸润癌分子时钟，以及 AI 驱动临床决策。

作者强调临床空间组学必须从 clinical question 和 endpoint 开始，而不是先做最炫的平台。不同问题需要不同设计：癌前病变需要纵向和阶段性采样；转移研究需要 primary tumor、不同 metastasis、正常组织和血液配对；MRD 需要治疗前后和复发前窗口；治疗反应研究需要 responder/non-responder 和治疗前/中/后样本。

样本保存方式直接决定平台选择。Fresh-frozen 更适合 discovery-level whole-transcriptome、metabolome 和 neoantigen 研究；FFPE 是临床回顾队列的主力，更适合 probe-based spatial transcriptomics 和高质量 histology。作者特别提醒 ischemia time、固定方式、切片厚度、paired blood/plasma、FFPE/fresh-frozen 配对等 pre-analytical variables 必须 protocolized。

临床应用方面，文章讨论了 pre-cancer、multi-site metastasis、MRD、biomarker 和 target discovery。对于癌前病变，空间组学可定位早期上皮状态变化、免疫抑制 niche 和 stromal remodeling；对于转移，可比较器官特异性微环境和克隆适应；对于 biomarker，可把空间结构转化为更可部署的 tissue-based 或 liquid biopsy marker。

#### Conclusions and future directions

作者最后认为，空间组学的瓶颈正在从“能不能测”转向“能不能标准化、扩展、解释和部署”。未来真正有临床价值的空间组学，不一定把高维原始空间数据原样推入临床，而是把 discovery-level 高维空间发现蒸馏为可扩展、可质控、AI-enabled、临床可部署的 assay。

关键挑战包括平台标准化、样本前处理一致性、跨平台可比性、成本和通量、空间数据分析 benchmark、空间模式的生物学可解释性、以及临床 endpoint 验证。作者的判断是，空间组学会成为 next-generation predictive and precision oncology 的核心组成，但前提是从漂亮图谱走向标准化临床研究设计。

### 作者结论与证据强度

作者较有力说明的是：空间组学技术已经形成多平台生态，能够在 RNA、蛋白、代谢、多模态和 3D 层面解析肿瘤组织；计算分析正在从细胞注释扩展到空间 niche、community、ecosystem 和临床关联；空间读数对癌前病变、转移、MRD、治疗反应和 biomarker discovery 具有明确转化潜力。

需要注意的是，本文是综述，不是单一原始研究。它的证据强度来自大量代表性研究和领域趋势整合，而不是作者自己生成的验证 cohort。因此，文中的 roadmap 和 conceptual hierarchy 很有指导价值，但某个具体空间 biomarker 是否能临床部署，仍需要癌种特异、平台特异、队列特异的独立验证。

## 独立方法学详解

### 综述型文章的证据结构

本文没有传统 Methods 章节，也没有单一原始数据集。它的方法学价值在于整理空间组学领域的技术分类、分析流程和临床研究设计原则。阅读时应把它当作“领域方法框架”和“临床转化路线图”，而不是把每个结论都当作同一实验体系下的统计结果。

综述的证据结构可以分为三层：第一，平台层证据，来自商业平台和技术论文；第二，分析层证据，来自空间数据处理、niche detection、多模态整合和 foundation model 相关方法；第三，肿瘤生物学和临床层证据，来自不同癌种的空间 profiling 研究。三层证据之间不是同质数据合并，因此不能做简单横向排名。

### 空间组学平台选择方法

平台选择首先取决于研究问题。若问题是“哪些细胞状态在组织里出现”，whole-transcriptome 或高通量 ST 更合适；若问题是“免疫检查点、靶点蛋白或细胞互作在哪里发生”，空间蛋白组更直接；若问题是“药物、脂质或代谢微环境如何分布”，空间代谢组不可替代；若问题是“空间结构如何影响克隆演化和治疗反应”，多模态整合更有价值。

第二个维度是样本。FFPE 支持大量临床回顾队列和病理图像配准，但通常适合 probe-based 或 targeted assay；fresh-frozen 支持更广发现层面的 RNA、代谢和部分多组学，但临床样本获取和保存要求更高。第三个维度是分辨率和区域大小。单细胞/亚细胞分辨率适合细胞互作和亚细胞定位，大面积低分辨率 capture 更适合全组织区域结构和大样本 cohort。

### 空间数据处理流程

空间数据处理的第一步是质量控制和坐标体系建立，包括图像质量、组织区域识别、背景去除、spot/cell/bin 的空间坐标和分子计数矩阵。成像型平台需要细胞分割；分割错误会直接影响细胞类型注释和细胞互作推断。spot/bin 平台需要 deconvolution 或 bin-to-cell reconstruction，否则一个空间单位可能混合多个细胞。

第二步是 normalization、batch correction 和 harmonization。空间数据的技术噪声来自组织厚度、探针效率、成像轮次、测序深度、组织保存和区域差异。第三步是特征增强，包括 resolution upscaling、missing gene imputation、feature augmentation 和 histology-aware enhancement。这些方法能提高可解释性，但也可能引入模型假设，因此必须保留原始数据对照。

### 统计学分析方法

作为综述，本文没有作者原创的统计检验、P 值或回归模型结果。它讨论的统计学和计算分析主要是空间组学研究中常用的方法框架。第一类是空间邻近和共定位分析：输入是细胞坐标、细胞类型或分子表达，目标是判断某些细胞类型是否比随机期望更常相邻或共定位。常见做法包括距离分布、nearest-neighbor enrichment、Ripley 类空间统计、permutation test 或 spatial autocorrelation。其局限是组织结构、细胞密度和采样区域会影响零分布。

第二类是空间 domain、niche 和 community 识别：输入是表达矩阵、细胞类型组成、空间邻接图和组织图像，目标是把组织划分成功能区域。方法可包括图聚类、隐变量模型、topic model、graph neural network 或 context-aware clustering。统计解释上，cluster/domain 是模型构建的空间单位，不是天然存在的实体；需要用 marker、病理区域、临床结局和独立样本验证。

第三类是空间细胞互作推断：输入是配体-受体表达、细胞坐标和邻接关系，目标是推断哪些细胞对可能发生信号通信。它比普通单细胞 ligand-receptor 分析多了空间约束，但仍不能证明真实蛋白接触或功能因果。更可靠的解释需要结合蛋白空间数据、功能实验或治疗扰动。

第四类是临床关联和预测模型：输入是空间特征，例如 TLS 成熟度、免疫 hub、CAF-tumor interface、MRD niche、drug target spatial distribution，以及患者结局或治疗反应。常见统计框架包括 Cox 回归、logistic regression、ROC/AUC、cross-validation、外部验证和 calibration。空间 biomarker 的最大风险是过拟合和平台依赖，因此必须有预设 endpoint、独立验证 cohort、标准化样本处理和可部署 assay。

### 空间计算模型和多模态整合

空间计算模型的核心挑战是把不同尺度的数据放到同一个组织坐标系。RNA、蛋白、代谢物、DNA 变异和 H&E 图像的空间分辨率、噪声结构和缺失机制不同。Horizontal integration 关注跨样本或跨 cohort 对齐；vertical integration 关注同一组织内不同模态整合；diagonal integration 关注不同样本、不同模态和不同空间分辨率同时对齐。

空间 foundation model 是未来方向之一。它试图从大量组织图像、空间表达和多模态数据中学习通用空间表示，再迁移到细胞注释、domain detection、预后预测和治疗反应建模。风险在于训练数据偏倚、跨平台泛化、模型可解释性和临床责任边界。对于医学应用，foundation model 不能只看 benchmark，还要看是否能提供稳定、可校准、可审计的临床输出。

### 临床转化研究设计

作者强调临床空间组学要从临床问题反推设计。如果目标是癌前病变进展预测，就需要 normal、precancer、invasive cancer 的阶段性样本和纵向随访；如果目标是转移机制，就需要 primary、multiple metastases、normal tissue 和血液/ctDNA 配对；如果目标是治疗反应，就需要治疗前、中、后样本，以及 responder/non-responder 的预设比较。

样本物流是临床空间组学成败的前提。需要预先规定 ischemia time、固定方法、切片厚度、染色流程、区域选择、病理标注和 paired biospecimen。分析上，应在 protocol 中预设 primary spatial endpoint，例如 TLS density、immune-excluded phenotype、target-positive tumor fraction、MRD niche score 或 spatial interaction signature，而不是事后在海量空间特征中寻找最显著结果。

### 可重复性资源和迁移注意点

迁移本文框架时，不能只复制某个平台名称。更重要的是把研究问题、样本类型、空间分辨率、模态选择和统计验证连成闭环。对于 FFPE 临床队列，优先考虑 probe-based ST、空间蛋白组和病理图像整合；对于 discovery 项目，fresh-frozen whole-transcriptome、代谢组或多模态平台更有价值。

复现空间组学研究时，必须报告平台版本、panel、组织保存方式、切片厚度、成像/测序深度、细胞分割方法、归一化流程、batch correction、空间邻接定义、统计零模型和验证 cohort。缺少这些信息时，空间图谱很难转化为可比较的 biomarker。

## 生物学与临床意义

这篇综述的生物学意义在于把肿瘤从“细胞组成问题”重新定义为“空间组织问题”。很多关键生物学现象不是某个细胞类型单独决定的，而是由细胞状态、邻近关系、组织结构和微环境压力共同决定。例如 TLS 是否成熟、T 细胞是否被排除在肿瘤边界外、CAF 是否形成免疫抑制屏障、药物靶点是否空间异质分布，这些都需要空间读数。

临床意义在于，空间组学可以帮助把 pathology、molecular oncology 和 AI 连接起来。未来临床可能不会直接报告成千上万个空间基因，而是报告经过验证的空间 biomarker：例如免疫 hub score、MRD niche score、drug target spatial coverage、tumor-stroma interface state 或 pre-invasive molecular clock。

## 局限性与危险假设

第一，空间组学图谱不等于机制证明。看到两类细胞相邻或一个 niche 与预后相关，只能提出机制假说，仍需要功能实验、扰动实验或纵向验证。

第二，平台差异会强烈影响结论。分辨率、panel、组织保存、细胞分割和归一化都会改变空间特征，因此跨平台比较必须谨慎。

第三，临床部署不能直接搬运 discovery-level 高维数据。高维空间发现需要被蒸馏为可质控、可解释、成本可接受、能在独立 cohort 复现的 assay。

第四，空间 AI 模型容易过拟合组织来源、染色流程和平台批次。没有外部验证、校准和可解释性，模型输出不能直接进入临床决策。

## 深度研究洞察

本文最重要的启发是将空间结构视为肿瘤生物学的“中间层”。基因突变、细胞状态和临床结局之间往往缺少直接桥梁；空间 niche 和 ecosystem 可能就是连接这些层级的组织机制。

第二个启发是，空间组学的价值不在于生成更复杂的数据，而在于把临床问题定位到组织结构中。对于早筛、癌前病变、MRD、转移和治疗反应，真正关键的是找到哪些空间结构代表进展风险、治疗脆弱性或可干预生态位。

第三个启发是，未来空间组学会与病理 AI 深度合流。H&E 图像提供低成本、可扩展形态信息；高维空间组学提供 discovery 和分子锚点；AI 的任务是把二者连接成临床可部署模型。

## 可借鉴或迁移的思路

对胃癌预防和 GIMs 研究，最值得迁移的是 Fig. 5 的临床转化路线。胃黏膜从 H. pylori 感染、慢性炎症、萎缩、肠化、异型增生到早癌，是典型的空间组织重塑过程。空间组学可用于构建 normal-inflammation-atrophy-IM-dysplasia-cancer 的分子时钟，识别哪些 epithelial state、immune niche、stromal boundary 或 microbial interface 预测进展。

具体设计上，可以用 FFPE 回顾队列做 targeted spatial transcriptomics 或 spatial proteomics，结合病理分区和随访结局，筛选可部署 biomarker；再用 fresh-frozen discovery cohort 做 whole-transcriptome 或多组学空间图谱，解释机制。统计上应预设 endpoint，如 GIM 进展、异型增生发生、早癌检出或根除后逆转，而不是只做横断面分组差异。

对免疫治疗研究，本文提示不要只看总体 T cell infiltration，而要看 T cell 是否进入肿瘤核心、是否接近 antigen-presenting cells、是否被 CAF 或髓系细胞隔离、是否形成 TLS 或 immune hub。空间结构可能比单纯细胞比例更接近治疗反应机制。

## 可复用学术表达

本文值得学习的表达是把 spatial omics 写成能够 reveal how tumor cells and the microenvironment are organized, interact, and evolve within tissues。这句话把空间组学的价值压缩成组织、互作和演化三个关键词。

第二个表达是把 spatially organized features 从 immune hubs 扩展到 microbiota and neural interfaces。这提醒写空间组学文章时，不要把空间只理解成肿瘤和免疫两类细胞的距离，而应扩展到组织生态系统。

第三个表达是 high-plex spatial discoveries may be distilled into scalable, AI-enabled, clinically deployable assays。这个表达非常适合转化医学：高维发现不是终点，临床部署需要蒸馏、标准化和可扩展。

## 相关论文与概念

空间转录组平台相关概念包括 imaging-based ST、sequencing-based ST、cyclic decoding、cyclic in situ sequencing、tissue-on-array capture 和 barcode-to-cell delivery。理解这些平台差异是设计空间研究的第一步。

空间计算相关概念包括 cell segmentation、deconvolution、spatial domain detection、spatially constrained clustering、cell-cell communication、spatial autocorrelation、multimodal integration、3D reconstruction 和 spatial foundation models。

肿瘤生态相关概念包括 TLS、tumor-stroma interface、immune-excluded phenotype、CAF niche、myeloid suppressive niche、vascular niche、hypoxia niche、microbiota-tumor interface 和 neural-tumor interface。

临床转化相关概念包括 pre-cancer atlas、MRD、multi-site metastasis profiling、longitudinal sampling、FFPE-compatible assay、TMA validation、spatial biomarker calibration、pathology AI 和 clinically deployable spatial assay。
