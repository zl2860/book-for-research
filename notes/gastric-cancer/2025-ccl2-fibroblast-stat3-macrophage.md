# Spatial dissection of tumour microenvironments in gastric cancers reveals the immunosuppressive crosstalk between CCL2+ fibroblasts and STAT3-activated macrophages

## 本文目录

- [基本信息](#基本信息)
- [本论文主图](#本论文主图)
- [生物学故事前情](#生物学故事前情)
- [重要缩写表](#重要缩写表)
- [论文详细解读](#论文详细解读)
  - [研究问题与科学背景](#研究问题与科学背景)
  - [研究设计与数据结构](#研究设计与数据结构)
  - [方法速览与分析框架](#方法速览与分析框架)
  - [原文结果完整梳理](#原文结果完整梳理)
    - [Spatial cellular maps of three GC subtypes](#spatial-cellular-maps-of-three-gc-subtypes)
    - [Spatially resolved cellular and transcriptional dynamics with respect to GC TME architecture](#spatially-resolved-cellular-and-transcriptional-dynamics-with-respect-to-gc-tme-architecture)
    - [Landscape of intercellular crosstalk and its functional consequences](#landscape-of-intercellular-crosstalk-and-its-functional-consequences)
    - [CCL2+ cancer-associated fibroblasts regulate JAK-STAT3 signalling in macrophages](#ccl2-cancer-associated-fibroblasts-regulate-jak-stat3-signalling-in-macrophages)
    - [CCL2+ CAFs recruit myeloid cells via STAT3-activated macrophages](#ccl2-cafs-recruit-myeloid-cells-via-stat3-activated-macrophages)
    - [CCL2+ fibroblast-mixed syngeneic mouse tumours recapitulate fibrotic GC](#ccl2-fibroblast-mixed-syngeneic-mouse-tumours-recapitulate-fibrotic-gc)
    - [Validation in a large GC cohort](#validation-in-a-large-gc-cohort)
  - [作者结论与证据强度](#作者结论与证据强度)
- [独立方法学详解](#独立方法学详解)
  - [研究对象、样本和数据结构](#研究对象样本和数据结构)
  - [实验流程和数据生成](#实验流程和数据生成)
  - [数据预处理和特征构建](#数据预处理和特征构建)
  - [统计学分析方法](#统计学分析方法)
  - [统计模型、机器学习模型或计算框架](#统计模型机器学习模型或计算框架)
  - [验证策略、稳健性和混杂控制](#验证策略稳健性和混杂控制)
  - [可重复性资源和迁移注意点](#可重复性资源和迁移注意点)
- [生物学与临床意义](#生物学与临床意义)
- [局限性与危险假设](#局限性与危险假设)
- [深度研究洞察](#深度研究洞察)
- [可借鉴或迁移的思路](#可借鉴或迁移的思路)
- [可复用学术表达](#可复用学术表达)
- [相关论文与概念](#相关论文与概念)
- [覆盖审计](#覆盖审计)

## 基本信息

- 期刊: Gut
- 年份: 2025，online first 2024-11-23
- 卷页: 74:714-727
- DOI: 10.1136/gutjnl-2024-332901
- 题名: Spatial dissection of tumour microenvironments in gastric cancers reveals the immunosuppressive crosstalk between CCL2+ fibroblasts and STAT3-activated macrophages
- 第一作者: Sung Hak Lee, Dagyeong Lee, Junyong Choi 等
- 通讯作者: Tae-Min Kim, Hoon Hur
- 研究领域: 胃癌、空间转录组、肿瘤微环境、CAF、巨噬细胞、免疫抑制、JAK-STAT3
- 关键词: gastric cancer, Visium, spatial transcriptomics, tumour microenvironment, CCL2, fibroblast, CAF, STAT3-activated macrophage, JAK-STAT3, fibrotic subtype
- 本地 PDF: `pdfs/processed/ccl2-fibroblast-stat3-macrophage-gastric-cancer.pdf`
- PDF 解析质量:
  - 使用 `scripts/build_pdf_llm_pack.py` 生成全文句子 ID。
  - 解析结果: 14 页，544 个句子；脚本标注 Results 39 句，Methods 163 句。
  - 重要纠偏: 由于 BMJ/Gut 排版把主文 Results 穿插在第 9-12 页并夹杂图注，脚本把大量真实 Results 句子误分到 `methods` 或 `supplementary`。本笔记按原文版面和小标题重新整理，纳入 `P002.S0017-P002.S0033`, `P009.S0001-P012.S0027` 等真实结果段。
  - 低置信内容: 图注、页眉页脚和版权提示混入正文；`P010.S0014-P011.S0001` 跨页断句；`P011.S0043-P012.S0001` western blot 句子跨页断裂；`P012.S0020-P012.S0021` 临床病理句跨页断裂；Fig. 6 图注和正文中 TMA 分组数、log-rank p 值存在轻微不一致。
  - Online supplemental methods: 主文提示详细方法在 online supplemental methods。期刊页面搜索结果可定位到 `gutjnl-2024-332901supp003.pdf`，但官方 BMJ 链接在本地访问时被 Cloudflare 403 拦截，本地目录也没有补充材料。因此本笔记的方法学只覆盖主文、图注和数据可用性可验证内容。
- 图像截取说明: 主图按整页渲染保存，避免漏 panel；后续需要局部 panel 时可再裁剪。
- LLM pack: `tmp/ccl2-fibroblast-stat3-macrophage-llm-pack.md`
- Manifest: `tmp/ccl2-fibroblast-stat3-macrophage-manifest.json`

---

## 本论文主图

| 原文图表 | 原文图题/核心信息 | 是否截取 | 图像文件 | 放置位置 |
|---|---|---|---|---|
| Fig. 1 | 9 例胃癌按空间细胞组成分为 epithelial、immunogenic、fibrotic 三类 | 是 | `assets/gastric-cancer/2025-ccl2-fibroblast-stat3-macrophage/page03.png` | [Spatial cellular maps of three GC subtypes](#spatial-cellular-maps-of-three-gc-subtypes) |
| Fig. 2 | 29,808 个 Visium spots 聚类为六类 spatial niches，并推断 niche 相关转录动态 | 是 | `page04.png` | [Spatially resolved cellular and transcriptional dynamics with respect to GC TME architecture](#spatially-resolved-cellular-and-transcriptional-dynamics-with-respect-to-gc-tme-architecture) |
| Fig. 3 | 构建 regulator-target cell crosstalk landscape，突出 fibroblast infiltration 与 IL6-JAK-STAT3/免疫检查点上调 | 是 | `page05.png` | [Landscape of intercellular crosstalk and its functional consequences](#landscape-of-intercellular-crosstalk-and-its-functional-consequences) |
| Fig. 4 | NicheNet、scRNA-seq、CellphoneDB、空间签名和外部队列支持 CCL2+ fibroblast 与 STAT3-activated macrophage 轴 | 是 | `page06.png` | [CCL2+ cancer-associated fibroblasts regulate JAK-STAT3 signalling in macrophages](#ccl2-cancer-associated-fibroblasts-regulate-jak-stat3-signalling-in-macrophages) |
| Fig. 5 | 体外验证 CAF/CCL2 促进单核细胞迁移、激活巨噬细胞 STAT3，并抑制 T 细胞 IFNG | 是 | `page07.png` | [CCL2+ CAFs recruit myeloid cells via STAT3-activated macrophages](#ccl2-cafs-recruit-myeloid-cells-via-stat3-activated-macrophages) |
| Fig. 6 | 小鼠同系移植和 675 例 TMA 验证 fibrotic GC 的巨噬细胞富集、CD8/GrzB 降低和差预后 | 是 | `page08.png` | [CCL2+ fibroblast-mixed syngeneic mouse tumours recapitulate fibrotic GC](#ccl2-fibroblast-mixed-syngeneic-mouse-tumours-recapitulate-fibrotic-gc) |
| Fig. 7 | 总结模型: CAF 促 EMT，招募并激活 macrophage STAT3，导致 T cell suppression | 是 | `page10.png` | [作者结论与证据强度](#作者结论与证据强度) |

## 生物学故事前情

胃癌的肿瘤微环境不是一团平均化的“免疫浸润”。同一块组织里，恶性上皮、成纤维细胞、内皮细胞、髓系细胞、T 细胞和 B/plasma cell 往往按组织结构分区出现。单细胞 RNA-seq 可以把细胞类型拆开，但会丢掉细胞在组织里的位置；传统病理能看到位置，却难以系统量化不同细胞之间的转录互作。

这篇文章的核心推进，是把胃癌 TME 从“有哪些细胞”推到“哪些细胞在什么空间生态位里互相调控”。作者先用 Visium 空间转录组在 9 例原发胃癌中建立细胞组成地图，再用 spot-level deconvolution 和邻近 spot 结构推断六类 spatial niches。真正的主线是 fibrotic GC: 这一类胃癌成纤维细胞多、T/plasma cell 少，空间上缺乏免疫细胞对 malignant-fibroblast 区域的分隔。

读这篇文章要抓住一个从现象到机制的链条：

1. 空间细胞组成把胃癌分成 epithelial、immunogenic、fibrotic 三类。
2. 六类 niches 揭示 fibroblast-infiltrated 区域是 EMT、血管生成、炎症和免疫抑制信号集中的区域。
3. 细胞互作模型把 fibroblast infiltration 指向 immune-cell IL6-JAK-STAT3 和 immune checkpoint 上调。
4. NicheNet 和 scRNA-seq 把关键配体/细胞对收敛到 CCL2+ fibroblast 和 STAT3-activated macrophage。
5. 体外迁移、pSTAT3、T cell IFNG 抑制，小鼠模型和 TMA 队列共同把这条轴从计算推断推向功能验证。

## 重要缩写表

| 缩写 | 中文含义 | 本文语境中的具体指代 | 阅读时注意 |
|---|---|---|---|
| GC | gastric cancer，胃癌 | 9 例 Visium 原发胃癌、公共胃癌转录组队列和 675 例 TMA 队列 | 不是单一分子亚型，包含 intestinal/diffuse、MSI/EBV 等异质背景 |
| TME | tumour microenvironment，肿瘤微环境 | 恶性细胞、CAF/ fibroblast、内皮、髓系、T/B/NK/plasma cell 等组成的空间生态 | 本文强调空间关系和功能互作，不只是细胞比例 |
| Visium | 10x Genomics 空间转录组平台 | 9 例 FFPE/组织切片上每个 spot 的表达和空间坐标 | spot 不是单细胞，需要 deconvolution |
| spot | 空间转录组采样点 | 每例 1,882-4,274 个 spot，9 例合计 29,808 个 spot | 每个 spot 可混合多种细胞 |
| CAF | cancer-associated fibroblast，癌相关成纤维细胞 | 本文主线中的 fibroblast/CAF，尤其 CCL2+ fibroblast | 文中有时用 fibroblast，有时用 CAF；功能验证主要用 CAF 细胞 |
| CCL2 | C-C motif chemokine ligand 2 | fibroblast 表达的关键 chemokine，NicheNet 指向 IL6-JAK-STAT3 免疫轴 | CCL2 阻断临床单药历史并不理想，本文更支持 subtype/联合策略假说 |
| STAT3-activated macrophage | STAT3 激活巨噬细胞 | JAK-STAT3 signature 高的 macrophage；scRNA-seq 中定义为 251 个 high-score macrophages | 是转录状态定义，不等于所有 pSTAT3 蛋白阳性巨噬细胞 |
| CF-high/SM-high | CCL2+ fibroblast high / STAT3-activated macrophage high | 外部 bulk 队列中两个 signature score 同时高的病例 | 依赖 signature deconvolution，不是直接空间检测 |
| iCAF/myCAF | inflammatory/myofibroblastic CAF | Fig. 4C 中用于解释 CCL2+ fibroblast 与既有 CAF 程序关系 | CCL2+ fibroblast 不应简单等同于 iCAF |
| NicheNet | 配体-靶基因推断框架 | 用 fibroblast ligand 解释 immune-cell IL6-JAK-STAT3 target genes | 预测调控关系，不是物理结合实验 |
| CellphoneDB | ligand-receptor 互作工具 | 比较 CCL2+ fibroblast 与 STAT3-activated macrophage 的 ligand-receptor 对数 | 依赖表达共现和数据库 |
| GSEA | gene set enrichment analysis | 对 cell type-specific inferred expression 做 Hallmark gene set 富集 | 输出是功能程序富集，不直接等于蛋白活性 |
| TMA | tissue microarray，组织芯片 | 675 例胃癌大队列 IHC 验证三类 subtype 和生存差异 | 主要是 histology/IHC 层面的验证，不是空间转录组 |
| PMA/ionomycin | T 细胞激活刺激 | 激活 Jurkat T cells，用 IFNG 作为激活读出 | Jurkat 是模型细胞，不等价于原代肿瘤 T 细胞 |
| GrzB | granzyme B | 小鼠肿瘤 IHC 中免疫激活/细胞毒读出 | 减少支持免疫抑制，但不是完整抗肿瘤免疫功能测定 |

## 论文详细解读

### 研究问题与科学背景

作者要解决的问题不是“胃癌 TME 中有没有 CAF 或 macrophage”，而是这些细胞如何按空间生态位组织，并造成什么功能后果。背景中，作者指出胃癌治疗虽然有 HER2/trastuzumab 这样的分子靶向范式，但整体转化收益有限；胃癌异质性很大程度来自转录和细胞组成异质性（`P001.S0033-P001.S0036`）。既往 scRNA-seq 已能解析细胞亚群，作者自己的前期工作还做过 diffuse-type GC 的 depth-aware scRNA-seq，但单细胞数据不能直接回答局部空间互作（`P002.S0007-P002.S0009`）。

因此本文采用 Visium 空间转录组分析 9 例胃癌，目标是把组织结构、细胞组成、细胞互作和功能后果放在同一张图里（`P002.S0010-P002.S0014`）。摘要中作者直接给出研究目标：将胃癌生态系统的空间组织翻译成 malignant、stromal 和 immune cells 的 functional interaction landscape（`P001.S0004-P001.S0006`）。

### 研究设计与数据结构

主数据是 9 例手术切除原发胃癌的 Visium 空间转录组。每个组织切片获得 1,882-4,274 个 spots，中位数 3,491；总计 29,808 个 spots 用于后续 niche 聚类（`P002.S0017-P002.S0019`, `P004.S0006`, `P009.S0002`）。

细胞注释使用作者既往 5 例胃癌 scRNA-seq 资源做 spot-level deconvolution。原始 11 类细胞中，上皮细胞被进一步拆成 malignant epithelium 和 normal epithelium，因此每个 spot 最终估计 12 类细胞丰度（`P002.S0020-P002.S0021`）。单细胞层面的补充验证还使用了 23,477 个 TME cells，其中包括 726 个 fibroblasts，用于定位 CCL2+ fibroblast 和 JAK-STAT3 high macrophage（`P006.S0009-P006.S0013`, `P011.S0009-P011.S0013`）。

验证数据包括四层。第一，公共 bulk-level RNA-seq/microarray 队列，主要是 ACRG 和 TCGA，以及 GSE13861、GSE16899、GSE16901、GSE18541（`P011.S0024-P011.S0029`）。第二，体外 CAF/THP-1/Jurkat/PBMC 实验验证 CCL2 促进迁移、STAT3 磷酸化和 T 细胞 IFNG 抑制（`P011.S0035-P012.S0005`）。第三，YTN3 小鼠胃癌细胞与 GFP+ mouse gastric fibroblast 混合接种的同系肿瘤模型（`P012.S0007-P012.S0016`）。第四，675 例胃癌 TMA 用 H&E/IHC 和部分 RNA-ISH/multiplex IHC 验证 fibrotic subtype、预后和 CCL2+ fibroblast/pSTAT3+ macrophage 共定位（`P012.S0017-P012.S0027`）。

### 方法速览与分析框架

本文的分析框架可以拆成三步。

第一步是“细胞组成分型”。作者对每个 spot 做 12 类细胞丰度 deconvolution，再按每例组织的细胞组成聚类，将 9 例 GC 分为 epithelial、immunogenic、fibrotic 三类（`P002.S0021-P002.S0027`, `P003.S0005-P003.S0011`）。这个分型不是传统 Lauren 或 TCGA 分型，而是空间细胞组成分型。

第二步是“空间 niche 和 cell type-specific expression”。作者把 29,808 个 spots 按本 spot 和邻近 spot 的细胞丰度做层次聚类，得到六类 niches：epithelial-dominant、malignant-dominant、fibroblast-dominant、malignant-infiltrated、fibroblast-infiltrated、immune-dominant（`P009.S0001-P009.S0016`）。再对五类主要细胞推断 cell type-specific expression，并在不同 niches 之间做 GSEA，找出 malignant cells、fibroblasts、endothelial cells 和 immune cells 的 niche-dependent transcriptional dynamics（`P009.S0017-P009.S0025`）。

第三步是“互作和机制收敛”。作者把每个 spot 及其 18 个邻近 spots 作为局部环境，用 regulator cell abundance 与 target cell functional score 的相关性构建 4 类细胞之间 16 种 regulator-target 关系（`P005.S0005-P005.S0013`, `P009.S0036-P010.S0014`）。随后用 NicheNet 在 fibroblast-to-immune 的 IL6-JAK-STAT3 轴上寻找 ligand，CCL2 排到最前；再用 scRNA-seq、CellphoneDB、spatial signature、RNA-ISH/IHC、生存队列和功能实验逐层验证（`P011.S0003-P012.S0027`）。

### 原文结果完整梳理

#### Spatial cellular maps of three GC subtypes

![Fig. 1 整页](../../assets/gastric-cancer/2025-ccl2-fibroblast-stat3-macrophage/page03.png)

中文图注（基于原文图注）：Fig. 1A 用 heatmap 和 bar plots 展示 9 例 GC 中 12 类细胞的丰度，并通过层次聚类将样本分成 epithelial、immunogenic、fibrotic 三类。Fig. 1B 选取 GC1、GC3、GC4 分别代表 immunogenic、epithelial、fibrotic GC，左侧为病理区域注释，中间为每个 spot 中占优势的 deconvoluted cell type，右侧为 cell-type abundance 的 spot-level correlation heatmap。缩写包括 DC、EBV、MSI-H、MSS、NK、PC 和 Treg（`P003.S0005-P003.S0011`）。

作者首先用 Visium 处理 9 例原发胃癌，获得每例 1,882-4,274 个 spots，中位数 3,491（`P002.S0017-P002.S0019`）。基于既往 scRNA-seq 参考进行 deconvolution 后，作者对 12 类细胞丰度进行聚类，得到三类胃癌空间生态：epithelial、immunogenic、fibrotic（`P002.S0020-P002.S0022`）。

这三类与组织学有一定对应关系，但不是完全等同于 Lauren 分型。intestinal-type GC 被分到 immunogenic 或 epithelial；所有 fibrotic GC 都是 diffuse-type（`P002.S0023`）。Epithelial GC 主要由 malignant 或 normal epithelial cells 组成（`P002.S0024`）。Immunogenic GC 包括 MSI-positive 或 EBV-positive 背景，CD4+ 和 CD8+ T cells 是主要免疫成分（`P002.S0025`）。Diffuse-type 中 GC4、GC6、GC9 被注释为 fibroblast 高浸润的 fibrotic GC（`P002.S0026`）。

这里的第一层结论是：空间细胞组成可以把胃癌拆成三个可解释的生态类型，尤其 fibrotic GC 不是简单“间质多”，而是一个 fibroblast-enriched、T cell/plasma cell 相对少的 TME 类型（`P002.S0027-P002.S0033`）。

#### Spatially resolved cellular and transcriptional dynamics with respect to GC TME architecture

![Fig. 2 整页](../../assets/gastric-cancer/2025-ccl2-fibroblast-stat3-macrophage/page04.png)

中文图注（基于原文图注）：Fig. 2A 将 9 例 GC 共 29,808 个 spots 按细胞组成和邻近结构聚类为六类 niches，并按 TME infiltration 和优势细胞类型命名。Fig. 2B 展示六类 niches 的细胞组成及其在三类 GC subtype 中的分布。Fig. 2C 展示 GC1 的 niche spatial map。Fig. 2D 用示意图说明 malignant cells 和 fibroblasts 在 isolated 或 intermingled niches 中如何用于推断 cell type-specific expression。Fig. 2E 验证 inferred expression 与 lineage markers 一致。Fig. 2F-G 展示四类主要细胞在不同 niches 中的 Hallmark GSEA 富集和相关基因表达，FDR < 0.1。Fig. 2H-I 展示 immune-related genes 和 CIBERSORT 估计的 22 类免疫细胞丰度（`P004.S0005-P004.S0018`）。

作者将每个 spot 及其区域邻接信息纳入层次聚类，得到六类 spatial niches（`P009.S0001-P009.S0003`）。上皮或恶性上皮为主的区域分别称为 epithelial-dominant 和 malignant-dominant niches；成纤维细胞为主的是 fibroblast-dominant niche；其余三个是 malignant-infiltrated、fibroblast-infiltrated 和 immune-dominant niches（`P009.S0004-P009.S0007`）。

空间上，GC1 中 malignant-dominant 和 fibroblast-dominant niches 各自局限，malignant-infiltrated 和 fibroblast-infiltrated niches 像过渡区，被 immune-dominant niches 围绕；epithelial-dominant niches 则像正常上皮岛状分布（`P009.S0009-P009.S0012`）。作者据此提出，胃癌空间架构主要由 malignant cells 与 fibroblasts 的主导关系塑造，immune cells 在 immunogenic/epithelial GC 中形成分界；fibrotic GC 的免疫细胞耗竭使这种分界减弱（`P009.S0013-P009.S0016`）。

为了看同一细胞类型在不同空间语境中的表达变化，作者对 malignant cells、normal epithelium、fibroblasts、endothelial cells 和 aggregated immune cells 做 cell type-specific expression 推断（`P009.S0017-P009.S0021`）。GSEA 显示，malignant-dominant niches 中 malignant cells 上调 coagulation；fibroblast-infiltrated niches 中 malignant cells 上调 EMT，并且 angiogenesis、allograft rejection 等程序在 malignant cells、fibroblasts、endothelial cells 和 immune cells 中更突出（`P009.S0022-P009.S0025`）。

最关键的是免疫读出。Fibroblast-infiltrated niches 中 immune exhaustion markers 包括 IDO1、CTLA4、PDCD1、EOMES 上调；进一步按免疫细胞类型 deconvolution 后，CTLA4 和 PDCD1 等 exhaustion markers 在 Treg 中上调（`P009.S0026-P009.S0028`）。同时 22 类免疫细胞 abundance 分析显示，fibroblast-infiltrated niches 中 B cells 和 myeloid cells，尤其 DC 和 macrophages 更丰富（`P009.S0029-P009.S0031`）。这为后文 CCL2+ fibroblast 和 macrophage 轴埋下伏笔。

#### Landscape of intercellular crosstalk and its functional consequences

![Fig. 3 整页](../../assets/gastric-cancer/2025-ccl2-fibroblast-stat3-macrophage/page05.png)

中文图注（基于原文图注）：Fig. 3A 展示 functional crosstalk 分析框架：每个 spot 加 18 个邻近 spots 用于推断五类主要细胞的 cell type-specific expression，再做 GSEA 生成 functional scores，最后用 regulator cell abundance 和 target cell functional scores 的相关性推断功能互作。Fig. 3B 展示 malignant、endothelial、immune、fibroblast 四类细胞两两互作形成的 16 类 functional consequences。Fig. 3C-D 将 spots 按 malignant 或 endothelial infiltration 分成五个 bins，计算 proliferation index。Fig. 3E-F 将 spots 按 fibroblast infiltration 分成五个 bins，展示八类 immune-related functions 和相关免疫基因表达（`P005.S0005-P005.S0019`）。

作者指出，niche 分析能显示某种 TME infiltration 与功能状态相关，但难以判断到底是哪类细胞作为 regulator 造成 target cell 的功能变化。因此他们建立了 regulator-target 细胞互作框架（`P009.S0036-P009.S0039`）。

Fig. 3B 中第一组信号是 proliferation。G2M checkpoint、MYC targets、E2F targets 等细胞增殖相关基因在 malignant 和 endothelial cells infiltration 作为 regulator 时上调（`P009.S0040-P009.S0044`）。这提示 TME 对 malignant/endothelial infiltration 的适应可能表现为细胞增殖增强（`P009.S0045-P010.S0001`）。

第二组信号是 immune-related functions。八类 immune-related Hallmark gene sets 随 fibroblast 和 immune cell infiltration 上调；其中由 fibroblast regulatory influence 指向 malignant/immune cells 的通路包括 TNF-alpha via NF-kappaB、IL6-JAK-STAT3、inflammatory response 和 complement（`P010.S0002-P010.S0005`）。作者随后专门按 fibroblast infiltration 五分位比较 immune functions，发现八类免疫相关 gene sets 均随 fibroblast infiltration 增加，IL6-JAK-STAT3 和 allograft rejection 尤其明显（`P010.S0010-P010.S0012`）。

基因层面也支持免疫状态改变。低 fibroblast infiltration spots 中 GZMA、GZMB 等 cytotoxic genes 更高；随着 fibroblast infiltration 增加，PDCD1、CTLA4、TIGIT 等 immune checkpoints 上升（`P010.S0013-P011.S0001`）。作者将这一结果解释为 fibroblasts 通过激活 target cells 中 JAK-STAT3 相关信号，推动免疫细胞 dysfunction 和免疫抑制 TME（`P011.S0002`）。

#### CCL2+ cancer-associated fibroblasts regulate JAK-STAT3 signalling in macrophages

![Fig. 4 整页](../../assets/gastric-cancer/2025-ccl2-fibroblast-stat3-macrophage/page06.png)

中文图注（基于原文图注）：Fig. 4A 用 NicheNet 分析 fibroblast-to-immune crosstalk，CCL2 在 fibroblast ligands 中具有最高 ligand activity，并连接到 target/receptor genes。Fig. 4B 在 716 个 scRNA-seq fibroblasts 中显示 CCL2 表达分布。Fig. 4C 比较 CCL2 与其他 ligand、iCAF score、myCAF score 及 IL6/ACTA2 markers 的关系。Fig. 4D 在 23,477 个 TME single cells 中显示 JAK-STAT3 signature 主要局限于 myeloid cells，进一步集中于 macrophages，并以 high JAK-STAT3 score 定义 STAT3-activated macrophages。Fig. 4E 比较 CCL2+ fibroblast/STAT3-activated macrophage 与对应阴性细胞间的 ligand-receptor pairs。Fig. 4F-G 展示两类 signature 在空间中的共定位和 spot-level correlation。Fig. 4H-I 展示 ACRG、TCGA 和四个 GEO 队列中 CF-high/SM-high 与差预后的关系（`P006.S0005-P006.S0020`）。

在 fibroblast 可能调节的免疫功能中，作者聚焦 IL6-JAK-STAT3，因为它与胃癌 TME 中促癌炎症反应相关（`P011.S0003`）。NicheNet 用 fibroblasts 中的 ligands 解释 immune cells 中的 target/receptor genes，结果 CCL2 成为最强 master regulator，连接到 LTB、SOCS1、SOCS3、STAT3、TGFB1 等 IL6-JAK-STAT3 相关 target genes，并具有最高 ligand activity（`P011.S0004-P011.S0008`）。

单细胞数据进一步收窄细胞对象。726 个 fibroblasts 中 CCL2 并非广泛表达，而是局限于一个 cluster（`P011.S0009`）。全 TME 23,477 个 single cells 中，高 JAK-STAT3 score 主要出现在 myeloid cells，尤其 macrophages；作者据此定义 251 个 STAT3-activated macrophages，并与其余 1,804 个 macrophages 区分（`P011.S0012-P011.S0013`）。

CellphoneDB 分析显示，在 CCL2、SAA1、CCL19、CCL21 等 top ligands 中，CCL2+ fibroblasts 与 STAT3-activated macrophages 之间的 interacting ligand-receptor gene pairs 比 CCL2-negative 对照更多（`P011.S0014`）。作者随后用 CIBERSORT signature matrix functions 分别得到 425 个 CCL2+ fibroblast signature genes 和 425 个 STAT3-activated macrophage signature genes，用于空间和 bulk 队列打分（`P011.S0015-P011.S0016`）。

空间层面，GC1 中 CCL2+ fibroblast signature 和 STAT3-activated macrophage signature 分布高度一致；跨 9 例所有 spots 的相关性热图也显示两者高度相关，并主要与 stromal cells 聚集（`P011.S0017-P011.S0020`）。作者还用 CCL2/COL1A1 dual RNA-ISH 和 pSTAT3/CD68 multiplex IHC 做了原位验证（`P011.S0021-P011.S0023`）。

临床层面，作者在 ACRG 和 TCGA 中发现大多数病例要么 CF-high/SM-high，要么 CF-low/SM-low，分别为 ACRG 84% 和 TCGA 87.6%，说明两个 signature scores 强相关（`P011.S0024-P011.S0026`）。CF-high/SM-high 患者总体生存更差，ACRG p=0.02，TCGA p=0.05，log-rank test；四个 GEO 队列也有类似趋势，GSE13861、GSE16899、GSE16901、GSE18541 的 p 值分别为 0.06、0.04、0.02、0.09（`P011.S0027-P011.S0029`）。这些结果支持 CCL2+ fibroblast 可能通过 STAT3-activated macrophage 促进胃癌进展和免疫抑制，但 bulk signature 仍不是直接空间检测（`P011.S0030`）。

#### CCL2+ CAFs recruit myeloid cells via STAT3-activated macrophages

![Fig. 5 整页](../../assets/gastric-cancer/2025-ccl2-fibroblast-stat3-macrophage/page07.png)

中文图注（基于原文图注）：Fig. 5A 显示 CAF-conditioned medium 增强 THP-1 单核细胞迁移，paired t-test，P < 0.05。Fig. 5B-C 显示 200 ng/mL anti-CCL2 neutralising antibody 和 CCL2 knockdown CAF-CM 均降低 THP-1 迁移，paired t-test，P < 0.05。Fig. 5D 显示 CAF-stimulated macrophages 中 JAK-STAT3 genes 上调。Fig. 5E 显示 CAF 或 100 ng/mL recombinant CCL2 诱导 PMA-differentiated macrophages 的 STAT3 phosphorylation。Fig. 5F-G 显示 CAF-stimulated macrophages 抑制 PMA/ionomycin 激活的 Jurkat T cells 中 IFNG 表达，Kruskal-Wallis test 加 uncorrected Dunn's post hoc test（`P007.S0005-P007.S0018`）。

为了把空间转录组推断推进到功能实验，作者首先发现多种 CAF 中 CCL2 转录水平高于 human immune 和 GC cell lines（`P011.S0035-P011.S0036`）。CAF-conditioned medium 显著增强 THP-1 迁移；anti-CCL2 中和抗体降低这种迁移；shRNA 敲低 CAF 中 CCL2 后，CAF-induced THP-1 migration 也下降；recombinant CCL2 则剂量依赖增强 THP-1 迁移（`P011.S0037-P011.S0040`）。

下一步是 macrophage STAT3。作者用 PMA 将 THP-1 分化为 macrophages，与 CAF 共培养后做转录分析，GSEA 显示 JAK-STAT3 pathway genes 上调；western blot 证实 CAF 共培养或 recombinant CCL2 处理均可增加 macrophages 中 STAT3 phosphorylation（`P011.S0041-P012.S0001`）。

最后是 T 细胞功能。PMA/ionomycin 激活 Jurkat T cells 会提高 IFNG；但与 CAF-stimulated macrophages 共培养后，IFNG 显著下降（`P012.S0002-P012.S0004`）。作者还在从人 PBMC 分化得到的 macrophages 和 cytotoxic T cells 中复现实验，支持 CAF-induced STAT3 activation 和 T cell activation inhibition 不是只发生在 THP-1/Jurkat 模型里（`P012.S0005-P012.S0006`）。注意，抽取文本把 IFNG 在一处写成 INFG，这是 OCR/排版抽取噪音。

#### CCL2+ fibroblast-mixed syngeneic mouse tumours recapitulate fibrotic GC

![Fig. 6 整页](../../assets/gastric-cancer/2025-ccl2-fibroblast-stat3-macrophage/page08.png)

中文图注（基于原文图注）：Fig. 6A 将 YTN3 mouse GC cells 单独或与 GFP+ mouse gastric fibroblasts 混合后皮下接种 C57BL/6J mice，并在 day 7、14、26 收获肿瘤。Fig. 6B 比较肿瘤重量，Mann-Whitney U test 和 t-test，图注标注 **P < 0.001。Fig. 6C 用 GFP 和 alpha-SMA IHC 证明混入 fibroblasts 持续存在并形成 fibrotic-like 组织。Fig. 6D 用 F4/80、CD8alpha、granzyme B IHC 评估 macrophages、CD8+ T cells 和细胞毒活性，QuPath 计数 ROI，t-test，P < 0.05。Fig. 6E 在 TMA 中用 H&E 和 pancytokeratin/CD45RB/actin IHC 标注三类 GC subtype，并做 Kaplan-Meier 生存分析（`P008.S0005-P008.S0019`）。

小鼠模型使用 YTN3 mouse GC cell line，单独接种或与 GFP+ mouse gastric fibroblast 混合接种。作者先筛选 CCL2，发现 GFP+ MGF 的 CCL2 表达最高；接种后在第 7、14、26 天收获肿瘤（`P012.S0007-P012.S0010`）。与 YTN3-only 相比，YTN3+MGF 混合肿瘤在第 14 天更大（`P012.S0011`）。GFP 和 smooth muscle actin IHC 证明混入 fibroblasts 能持续存在，并使肿瘤呈现 fibrotic subtype GC 特征（`P012.S0012-P012.S0013`）。

免疫染色显示，MGF-mixed tumours 中 macrophages 富集，同时肿瘤中心区域 CD8+ T cells 和 GrzB+ cells 减少（`P012.S0014-P012.S0015`）。作者据此认为，CCL2+ fibroblasts 能增强 syngeneic tumours 中 macrophage accumulation，并贡献于 immunosuppressive TME（`P012.S0016`）。

这个动物实验的价值在于把“空间共定位和体外迁移”连接到活体肿瘤中的组织结构和免疫读出。它的边界也很清楚：这是皮下同系模型，不是胃原位肿瘤；用的是 mouse gastric fibroblast 与 YTN3 的混合接种，不能完全复现人类 diffuse/fibrotic GC 的发生过程。

#### Validation in a large GC cohort

作者进一步用 675 例胃癌 TMA 做 histological validation。按 IHC 中 pancytokeratin、CD45RB、actin 哪一个最高，把病例分为 epithelial、immunogenic 和 fibrotic 三类。正文给出的分组数为 228、126、321 例；Fig. 6 图注写作 226、126、320 例，存在轻微不一致，应按原文记录为一个低置信点（`P012.S0017-P012.S0019`, `P008.S0015-P008.S0018`）。

临床病理关联上，epithelial subgroup 中 differentiated-type GC 更多，immunogenic subgroup 中 undifferentiated-type GC 占比更高；MSI-H 更常见于 epithelial subtype，EBV-positive 更常见于 immunogenic subtype，p 值分别为 <0.001 和 0.004（`P012.S0020-P012.S0022`）。

生存分析显示 fibrotic subtype 预后差于 non-fibrotic subtypes。正文写 log-rank p=0.015，Fig. 6E 图注写 p=0.0023，这也是需要回看原图/统计表确认的点（`P012.S0023-P012.S0025`, `P008.S0019`）。此外，作者在 TMA 子集上用 RNA-ISH 和 multiplex IHC 进一步确认 CCL2+ fibroblasts 与 pSTAT3+ macrophages 共定位，支持 Visium 空间转录组发现具有临床组织学意义（`P012.S0026-P012.S0027`）。

### 作者结论与证据强度

![Fig. 7 整页](../../assets/gastric-cancer/2025-ccl2-fibroblast-stat3-macrophage/page10.png)

作者已经较强支持的内容：

- 9 例 GC 空间转录组可按细胞组成分成 epithelial、immunogenic、fibrotic 三类，fibrotic GC 具有 fibroblast enrichment 和较少 T/plasma cell infiltration（`P002.S0021-P002.S0033`）。
- 29,808 个 spots 可以组织成六类 niches，fibroblast-infiltrated niches 中 malignant cells 的 EMT、免疫 exhaustion/checkpoint、myeloid/B cell abundance 等信号增强（`P009.S0001-P009.S0031`）。
- Functional crosstalk 框架把 fibroblast infiltration 与 immune-cell IL6-JAK-STAT3、inflammatory response、checkpoint upregulation 联系起来（`P009.S0036-P011.S0002`）。
- NicheNet、scRNA-seq、CellphoneDB、spatial signature 和 RNA-ISH/IHC 均支持 CCL2+ fibroblasts 与 STAT3-activated macrophages 是一个空间相邻、功能相关的细胞对（`P011.S0003-P011.S0023`）。
- CAF/CCL2 促进 THP-1 migration，CAF 或 recombinant CCL2 激活 macrophage pSTAT3，CAF-stimulated macrophages 抑制 T cell IFNG，这些体外结果支持机制链条（`P011.S0035-P012.S0006`）。
- 小鼠 YTN3+MGF 模型和 675 例 TMA 支持 fibrotic-like TME 中 macrophage accumulation、CD8/GrzB 降低和差预后（`P012.S0007-P012.S0027`）。

合理但仍需谨慎的推断：

- CCL2+ fibroblast 是 fibrotic GC 免疫冷环境的关键组织者。
- STAT3-activated macrophage 是 CCL2+ fibroblast 介导免疫抑制的主要执行细胞。
- CCL2/CCR2 或 CCL2-macrophage-STAT3 轴可能与免疫检查点治疗联用，尤其适合 fibrotic subtype GC。

尚未完全证明的内容：

- 在人类胃癌原位环境中，阻断 CCL2 或 CCR2 是否能解除免疫抑制并提高 ICI 反应。
- CCL2+ fibroblast 和 STAT3-activated macrophage 是否是 fibrotic GC 差预后的独立因果因素，而不是 fibroblast-rich/diffuse histology 的伴随标志。
- Visium spot-level deconvolution 对 T cell subpopulation 的解析有限，不能充分证明 CD8 T cell exhaustion 或 Treg-specific dynamics。

## 独立方法学详解

### 研究对象、样本和数据结构

主空间队列为 9 例手术切除原发胃癌，使用 10x Genomics Visium 空间转录组。每个切片 1,882-4,274 个 spots，中位 3,491（`P002.S0017-P002.S0019`）。作者没有在主文中展开纳排标准和样本处理细节，而是指向 online supplemental methods；由于补充材料未能获取，本节不补写无法验证的实验细节（`P002.S0015`）。

scRNA-seq 参考来自作者此前 5 例 GC 数据。主文明确提到 726 个 fibroblasts 和 23,477 个 TME single cells 用于 CCL2+ fibroblast 与 JAK-STAT3 high macrophage 分析（`P011.S0009-P011.S0013`）。这个参考数据承担两个角色：一是用于 Visium spot deconvolution，二是用于构建 CCL2+ fibroblast 和 STAT3-activated macrophage 细胞状态。

外部临床验证包括 ACRG、TCGA 和四个 GEO 队列，结局为 overall survival；TMA 队列包含 675 例 GC，用 IHC 分型并做生存分析（`P011.S0024-P011.S0029`, `P012.S0017-P012.S0025`）。

### 实验流程和数据生成

空间转录组流程的主文可见步骤包括：Visium 生成每个 spot 的表达数据；基于 scRNA-seq 参考对 11 类细胞做 deconvolution；将上皮细胞进一步拆成 malignant 和 normal epithelium，得到 12 类细胞丰度（`P002.S0020-P002.S0021`）。

体外实验包括三组：第一组是 THP-1 transwell migration，用 CAF-conditioned medium、anti-CCL2 neutralising antibody、CCL2 knockdown CAF-CM 和 recombinant CCL2 测试迁移变化（`P007.S0006-P007.S0009`, `P011.S0037-P011.S0040`）。第二组是 THP-1-derived macrophage 与 CAF 共培养，检测 JAK-STAT3 transcriptional enrichment 和 pSTAT3 western blot（`P007.S0010-P007.S0012`, `P011.S0041-P012.S0001`）。第三组是 activated Jurkat T cells 或 PBMC-derived cytotoxic T cells，与 CAF-stimulated macrophages 共培养，读出 IFNG（`P007.S0013-P007.S0017`, `P012.S0002-P012.S0005`）。

动物实验为 C57BL/6J 小鼠皮下同系肿瘤模型，YTN3 cells 单独或与 GFP+ MGF 混合注射，day 7、14、26 收获。IHC 标记 GFP、alpha-SMA、F4/80、CD8alpha、granzyme B，并用 QuPath 计数 ROI（`P008.S0006-P008.S0014`, `P012.S0007-P012.S0015`）。

### 数据预处理和特征构建

细胞组成分型的输入是每例样本中 12 类细胞的 spot-level abundance。层次聚类产生 epithelial、immunogenic、fibrotic 三类 GC（`P002.S0021-P002.S0027`）。

Spatial niche 构建的输入是每个 spot 和邻近 spots 的细胞组成。29,808 个 spots 被分为六类 niches，并按优势细胞和 TME infiltration 命名（`P009.S0001-P009.S0007`）。

Cell type-specific expression 推断的对象是五类主要细胞：malignant cells、normal epithelium、fibroblasts、endothelial cells 和 aggregated immune cells。作者通过 lineage marker concordance 验证推断表达大体符合细胞谱系（`P009.S0017-P009.S0022`）。

CCL2+ fibroblast 和 STAT3-activated macrophage 的 signature 构建基于 scRNA-seq：CCL2+ fibroblast 来自 CCL2 局部高表达 fibroblast cluster；STAT3-activated macrophage 定义为 JAK-STAT3 score 高的 251 个 macrophages。作者随后使用 CIBERSORT signature matrix functions 为两类细胞各构建 425 个 signature genes（`P011.S0009-P011.S0015`）。

### 统计学分析方法

层次聚类用于样本 subtype 和 spot niche 分类。输入是细胞丰度矩阵，输出是聚类标签；它能生成数据驱动的分组，但分组数和距离度量会影响结果，不能自动证明这些 subtype 是天然离散类别（`P002.S0021-P002.S0023`, `P009.S0001-P009.S0007`）。

GSEA 用于评估不同 niches 或实验条件下的 functional programs。Fig. 2 中使用 Hallmark gene sets，FDR < 0.1 作为富集阈值；Fig. 5D 用于比较 CAF-stimulated macrophages 和 non-stimulated macrophages 的 JAK-STAT3 genes（`P004.S0014`, `P007.S0010`, `P009.S0022`, `P011.S0042`）。GSEA 的结论是基因集层面的趋势，不能替代蛋白活性测定，因此作者用 pSTAT3 western blot 补强。

相关分析用于 functional crosstalk 和空间共定位。Functional crosstalk 中，regulator cell abundance 与 target cell functional scores 的相关性被解释为功能关系；Fig. 4G 中，CCL2+ fibroblast 和 STAT3-activated macrophage signature 与 12 类细胞丰度做 spot-level correlation（`P005.S0009-P005.S0011`, `P006.S0016-P006.S0017`, `P011.S0016-P011.S0019`）。相关性不能证明方向性，所以作者又加入 NicheNet、CellphoneDB 和实验扰动。

生存分析使用 Kaplan-Meier 和 log-rank test。ACRG/TCGA 中比较 CF-high/SM-high 与 CF-low/SM-low 的 overall survival，p=0.02 和 p=0.05；四个 GEO 队列 p=0.06、0.04、0.02、0.09；TMA 中 fibrotic subtype 预后更差，正文 p=0.015（`P011.S0027-P011.S0029`, `P012.S0023-P012.S0024`）。这些是预后相关性，不是独立多变量因果证明。

体外迁移实验使用 paired t-test，anti-CCL2 和 knockdown 比较也用 paired t-test；Jurkat IFNG 实验使用 Kruskal-Wallis test 加 uncorrected Dunn's post hoc test；小鼠肿瘤重量用 Mann-Whitney U test 和 t-test，IHC ROI 计数用 t-test（`P007.S0006-P007.S0017`, `P008.S0008-P008.S0014`）。这些统计适合小规模实验比较，但样本量、重复数和效应大小需回补充材料确认。

### 统计模型、机器学习模型或计算框架

Visium deconvolution 是本文所有空间结论的基础。它把混合 spot 表达拆成细胞类型丰度和部分 cell type-specific expression。优势是能利用已有 scRNA-seq 参考恢复组织空间结构；风险是 spot 内细胞混合、参考数据偏差和低分辨率会影响 T cell subpopulation、macrophage state 等细粒度状态。

NicheNet 回答的问题是：fibroblasts 中哪些 ligands 最能解释 immune cells 中 IL6-JAK-STAT3 target genes 的变化。它输出 ligand activity 和 ligand-target/receptor 关系；本文中 CCL2 排名最高（`P011.S0003-P011.S0008`）。NicheNet 是有方向的调控推断，但依赖数据库和表达数据，因此需要功能验证。

CellphoneDB 回答的是 ligand-receptor pairs 是否在两个细胞群之间表达并形成潜在互作。本文用它比较 CCL2+ fibroblast/STAT3-activated macrophage 与对应阴性细胞对，发现前者互作对更多（`P011.S0014`）。这支持两类细胞在分子层面可互作，但不能证明 CCL2 单独驱动所有 STAT3 activation。

CIBERSORT signature matrix functions 用于构建两类细胞 signature，并把它们投射到空间 spots 和 bulk cohorts 中（`P011.S0015-P011.S0027`）。这种迁移能放大样本量和临床结局信息，但 bulk 队列里 CF-high/SM-high 是 signature 高，不等于真实细胞邻近。

### 验证策略、稳健性和混杂控制

本文的验证策略是多层证据链，而不是单一大队列验证。

空间发现先用 scRNA-seq 参考和 Visium spots 形成计算推断，再用 RNA-ISH 和 multiplex IHC 原位验证 CCL2/COL1A1 与 pSTAT3/CD68（`P011.S0021-P011.S0023`, `P012.S0026-P012.S0027`）。预后关联用 ACRG、TCGA 和四个 GEO 队列重复观察（`P011.S0024-P011.S0029`）。功能因果方向通过 CCL2 antibody、CCL2 knockdown、recombinant CCL2、pSTAT3 western blot 和 T cell IFNG 抑制实验补强（`P011.S0037-P012.S0005`）。组织生态层面用 syngeneic mouse model 和 675 例 TMA 验证 fibrotic GC 的免疫抑制特征（`P012.S0007-P012.S0027`）。

混杂控制仍有限。比如 fibrotic subtype 与 diffuse histology、stromal abundance、低 T cell infiltration、肿瘤阶段等可能共同变化；公开队列 signature 生存分析未在主文中显示充分多变量 Cox；TMA 分型使用 protein abundance 最高者分类，可能与传统病理类型、分期和治疗差异混杂。

### 可重复性资源和迁移注意点

数据可用性声明显示，研究使用的公共数据来自 TCGA 和 GEO，列出的 accession 包括 GSE62254、GSE13861、GSE268999、GSE26901、GSE28541；本研究测序数据上传至 GEO，accession ID 为 GSE251950（`P014.S0001-P014.S0004`）。注意主文中的 GEO 编号 `GSE26901` 和前文 cohort 名 `GSE16901` 不完全一致，复现时需要到 GEO 和补充材料核对。

将这套方法迁移到自己的胃癌研究时，至少需要三类输入：空间转录组坐标和表达矩阵、匹配癌种/平台的 scRNA-seq reference、足够可靠的病理区域注释或组织结构标签。最容易出错的是把 Visium spot-level inferred states 当成单细胞真实状态，尤其在 macrophage activation、Treg exhaustion、CD8 dysfunction 这类细胞状态上。

## 生物学与临床意义

本文把 fibrotic GC 的免疫冷环境解释为一个空间互作问题：CAF 不只是形成物理基质，也通过 CCL2 招募 myeloid cells，并在 macrophages 中诱导 STAT3 activation，进而抑制 T cell activation。这比“CAF 多所以免疫差”更具体，因为它给出了可检测细胞对、配体、受体/信号通路和功能读出。

临床上，CCL2+ fibroblast/STAT3-activated macrophage signature 与差预后相关，且 fibrotic subtype 在 675 例 TMA 中也有不良生存。这提示 fibrotic GC 可能需要 stromal-myeloid directed immunotherapy，而不是单纯依赖 PD-1/PD-L1。作者讨论中也提到，既往 CCL2 单抗 carlumab 在终末期实体瘤单药效果不佳，但在 fibrotic subtype GC 中与 ICI 联用可能更值得测试（`P013.S0014-P013.S0019`）。

转化边界是：目前还没有证明 CCL2/CCR2 或 STAT3 轴在胃癌患者中被阻断后能改变免疫治疗结局。现阶段更适合作为患者分层、机制假说和联合治疗设计依据，而不是立即作为临床靶点。

## 局限性与危险假设

第一，主空间队列只有 9 例 GC。它适合发现空间生态和机制假说，但不足以独立定义稳定的临床分型。

第二，Visium 的 spot 分辨率限制明显。作者自己在 discussion 中承认，deconvolution 技术限制使 cytotoxic T cells 等 T cell subpopulations 的 transcriptional dynamics 未被充分评估，需要更高分辨率空间平台（`P013.S0002-P013.S0004`）。

第三，CCL2+ fibroblast 与 STAT3-activated macrophage 的因果链条虽然有体外和小鼠支持，但人类原位因果仍未闭环。特别是 macrophage STAT3 activation 可能也受 IL6、CSF1、hypoxia、necrosis、tumor-derived factors 等影响。

第四，公开 bulk 队列中的 CF-high/SM-high 是 signature 推断，不是空间共定位。bulk signature 高也可能只是 fibrotic/diffuse/stromal-rich 肿瘤的伴随特征。

第五，TMA 分型和生存结果存在文本与图注数字不一致，包括 epithelial/fibrotic 分组数和 log-rank p 值。结论方向一致，但精确引用时必须回看补充表或原始统计。

## 深度研究洞察

这篇文章最值得学习的不是某一个工具，而是“空间生态位到功能机制”的证据路线。作者没有停留在 Visium clustering，而是把 spot niches、cell type-specific expression、regulator-target crosstalk、ligand-receptor inference、scRNA-seq 状态定义、空间 signature、原位验证、外部队列预后、体外扰动和小鼠模型串成一条链。

另一个关键点是它把 CAF 的作用从“屏障/ECM”扩展到“髓系免疫编程”。在很多胃癌免疫研究中，T cell exhaustion 或 checkpoint upregulation 是终点；本文往上游追问这些免疫状态可能由哪个空间细胞对组织起来，最终落到 CCL2+ fibroblast 和 STAT3 macrophage。

这对后续研究有两个启发。第一，fibrotic subtype 不应只用 bulk stromal score 定义，而应拆成空间结构、CAF 状态和 myeloid activation 三个层面。第二，免疫治疗耐药研究不应只盯 T cell intrinsic exhaustion，还要识别谁在局部生态位中持续激活 suppressive myeloid programs。

## 可借鉴或迁移的思路

- 用空间数据做“细胞组成分型”，再用大 TMA/IHC 队列验证分型可见性和预后意义。
- 把 Visium spot 的局部邻域纳入 niche 聚类，而不是只看单 spot 表达。
- 先用 regulator-target functional landscape 筛方向，再用 NicheNet/CellphoneDB 把方向收敛到 ligand 和 cell pair。
- 在 bulk 队列中用 cell-state signature 做外部预后验证，但必须明确这不是空间共定位验证。
- 对空间组学推断出的关键轴，至少做一个分子扰动、一个功能读出和一个组织/动物层面的验证。
- 对 fibrotic GC 或 diffuse GC，可以优先检查 CCL2+ CAF、pSTAT3+ CD68 macrophage、CD8/GrzB spatial exclusion 和 PDCD1/CTLA4/TIGIT 免疫状态。

## 可复用学术表达

本文有几个表达策略值得复用：

- 先定义“cellular composition-based subtype”，再说明它与传统 Lauren/MSI/EBV 分类的关系，而不是让新分型悬空。
- 用“regulator cells”和“target cells”区分细胞互作中的方向性假设，便于把相关性分析组织成可验证模型。
- 把“spatial co-localisation”和“clinical association”分开写，避免把位置相邻直接说成临床因果。
- 在 discussion 中主动指出 Visium/deconvolution 对 T cell subpopulation 的限制，这使结论边界更清楚。

## 相关论文与概念

- 作者既往 diffuse-type GC depth-aware scRNA-seq: 本文多处复用该 scRNA-seq 参考，并从 superficial/deep layer 进展模型转向真正空间转录组（`P002.S0007-P002.S0008`）。
- NicheNet: 用于从 target gene program 反推 upstream ligand。
- CellphoneDB: 用于 ligand-receptor interaction pair 统计。
- CCL2-CCR2 axis: 经典 monocyte/macrophage recruitment 轴，肿瘤免疫中常与 suppressive myeloid cells、MDSC、TAM 相关。
- IL6-JAK-STAT3: 髓系促癌炎症和免疫抑制的重要信号通路，本研究把其空间来源指向 fibroblast-rich niches。
- Fibrotic / immune-cold gastric cancer: 与 CAF enrichment、T cell exclusion、低 ICI 反应潜力相关，适合设计 stromal-myeloid targeted combination therapy。

## 覆盖审计

- 全文抽取: 14 页，544 个句子。
- 主文 Results 覆盖:
  - 摘要 Results: `P001.S0007-P001.S0013`
  - 三类 GC subtype: `P002.S0017-P002.S0033`
  - Fig. 1-6 图注: `P003.S0005-P008.S0019`
  - Spatial niches 和 transcriptional dynamics: `P009.S0001-P009.S0031`
  - Intercellular crosstalk: `P009.S0036-P011.S0002`
  - CCL2+ fibroblast/STAT3 macrophage 轴: `P011.S0003-P011.S0030`
  - 体外验证: `P011.S0035-P012.S0006`
  - 小鼠与 TMA 验证: `P012.S0007-P012.S0027`
- Methods 覆盖:
  - 主文 Methods 只有 `P002.S0015-P002.S0016`，详细 online supplemental methods 未包含在用户给定 PDF 中，官方 supplement 下载受 403 阻断，因此未做不可验证扩写。
  - 图注中的方法和统计信息已覆盖 `P004.S0014`, `P005.S0005-P005.S0019`, `P006.S0005-P006.S0020`, `P007.S0005-P007.S0018`, `P008.S0005-P008.S0019`。
- Discussion 覆盖:
  - 主要方法限制、Visium/deconvolution 局限、CCL2/ICI 转化意义覆盖 `P012.S0032-P013.S0022`。
- 未覆盖或弱覆盖:
  - References、author affiliations、copyright/Downloaded/page header 等非科学内容未逐句解释。
  - Online supplemental notes、supplemental figures/tables 的具体内容没有获取，所有相关结论均按主文引用边界处理。
- 低置信/需回看原文:
  - `P010.S0014-P011.S0001`: immune checkpoint 句与 Fig. 7 图注混排。
  - `P011.S0043-P012.S0001`: western blot 结果跨页断句。
  - `P012.S0020-P012.S0021`: clinicopathological association 跨页断句。
  - Fig. 6 图注与正文 TMA 分组数不一致: 226/126/320 vs 228/126/321。
  - Fig. 6 survival p 值图注和正文不一致: p=0.0023 vs p=0.015。
