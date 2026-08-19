# Mutational Signatures and Clonal Hematopoiesis in Intestinal Metaplasia across Countries with Varying Stomach Cancer Incidence

<!-- wechat-style-reviewed: 2026-08-19 -->

发现胃肠化生以后，临床上最难回答的问题往往不是“它是不是癌前病变”，而是“这个人究竟有多大概率会继续进展”。

大多数胃肠化生长期稳定，只有少数病灶会走向异型增生或早期胃癌。如果所有患者都接受同样密集的胃镜随访，成本和负担很高；如果只依赖年龄、幽门螺杆菌和胃肠化生评估系统（OLGIM）分期，又可能漏掉已经开始克隆演化的高危病灶。

地区差异让问题更复杂。日本、韩国等胃癌高风险地区，与新加坡、北美等中低风险地区相比，不仅发病率不同，幽门螺杆菌菌株、上皮突变过程和宿主炎症背景也可能不同。

这项研究分析了 1,582 个胃肠化生样本。作者给出的答案是：高深度测序可以找到低频上皮克隆，其中 ARID1A 截短突变与早期胃肿瘤相关；SBS17 突变签名和高水平克隆性造血提供了额外的风险线索。把分子变量加入临床模型后，受试者工作特征曲线下面积（AUC）从 0.72 升至 0.773，但模型只有 26 例早期胃肿瘤事件，尚不能直接改变随访方案。

## 01｜只看幽门螺杆菌，为什么还不够

幽门螺杆菌（Hp）是胃癌最重要的危险因素之一，但感染状态无法解释所有个体差异。胃肠化生形成后，胃内环境已经改变，细菌丰度可能下降；一次检测阴性也不等于从未感染。

作者在高风险地区观察到更高的高丰度 Hp 检出率：韩国近期队列为 24/106，日本为 2/33，而近期新加坡队列为 3/218。日本和韩国菌株还在 CagA N 端变异上与新加坡菌株分离，高风险地区 CagA variant 与 ASPP2 的结合更强。

这说明问题不只是“有没有 Hp”。感染年代、菌株毒力和宿主上皮已经积累的分子改变，都可能影响后续风险。

## 02｜这项研究到底做了多大规模

研究以 1,582 个胃肠化生（IM）样本和 98 个正常胃样本为主体。靶向基因面板（panel）覆盖 277 个人基因和 6 个 Hp 基因，平均测序深度达到 1,108×。

近期招募的胃窦胃肠化生来自新加坡、韩国、香港、美国、日本和台湾；作者同时加入既往新加坡 TransGCEP1000 队列。除此之外，20 对 IM–normal 样本进行了平均 60.5× 的全基因组测序（WGS），韩国 14 名患者的正常、异型增生和早期胃癌样本接受了酶促甲基化测序（EM-seq）。

转录组、单细胞、胃与唾液微生物组、类器官、FISH 和 Stereo-seq 并不是彼此独立的展示。它们围绕同一条主线工作：先用高深度 DNA 测序寻找低频克隆，再用多模态数据解释这些克隆可能对应的细胞状态和黏膜生态。

## 03｜为什么普通测序深度可能看不见风险

胃肠化生中的体细胞突变等位基因频率很低。作者比较后发现，全基因组测序只能恢复高深度 panel 检出的 17.5% 体细胞突变；模拟 100× 全外显子组测序（WES）只能恢复 15.5% 体细胞突变，以及 15.1% 可能改变蛋白的驱动突变。

这不是单纯的技术细节。如果测序深度不够，最早期、最小的异常克隆会直接从数据里消失，研究者可能误以为癌前组织没有 driver。

高深度 panel 最终识别到 47 个显著突变基因和 2,100 个驱动突变（driver mutations），其中 25 个基因此前未在胃肠化生中报告。

## 04｜哪些上皮 driver 真正关联早期胃肿瘤

在 Fig. 2 汇总的 1,095 个胃窦 IM 中，日本/韩国受试者的每样本体细胞突变数中位数为 28.5，中国受试者为 20（Wilcoxon P = 4.1 × 10^-11）；地区频率部分比较中国样本 909 例与日本/韩国样本 142 例。跨地区合并的 EGN 分析比较 ARID1A truncating mutation 携带者与未携带者：携带者发生同期或后续 early gastric neoplasia（EGN，高级别异型增生或早期胃癌）的优势比为 6.2（P = 1.5 × 10^-3）。

![Fig. 2：跨地区 driver landscape 与 ARID1A 风险](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig2-page7.png)

简明图注：Fig. 2 的 driver 图谱覆盖 1,095 个胃窦 IM，地区频率比较包括中国样本 909 例和日本/韩国样本 142 例；跨地区合并后，ARID1A 截短突变携带者相对未携带者更常见同期或后续 EGN（OR = 6.2，P = 1.5 × 10^-3）。这是队列内关联，不是已经外部纵向验证的预测标志。

## 05｜KRAS–MAPK 改变能否提供干预线索

另一组改变落在 KRAS–MAPK 通路。104 个同时有靶向 DNA 和 bulk RNA-seq 的 IM 中，10 个带有 KRAS/MAPK driver alterations；与其余 94 个样本相比，它们的 KRAS、ERK 和交集 signature 均升高。把对照随机下采样为 10 个、重复 1,000 次后，KRAS–ERK signature 仍有 983 次方向一致。

作者建立了 6 个 IM 和 4 个正常胃来源类器官；Fig. 3G 的 1 μmol/L、72 小时活力实验实际比较每组 4 个生物学重复，IM 类器官活力下降更多（线性混合效应模型 P < 0.0005）。但单独抑制 ERK 或 STAT3 没有复现这种选择性，因此不能把结果简化成某一条通路已经成为癌前治疗靶点。

![Fig. 3：KRAS–MAPK 改变、细胞状态与类器官实验](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig3-page9.png)

简明图注：Fig. 3 的 bulk 比较为 10 个带 KRAS/MAPK driver alterations 的 IM 对 94 个无可检出改变的 IM；类器官共建立 6 个 IM 和 4 个正常胃来源，Fig. 3G 的药物活力实验则为每组 4 个生物学重复。转录程序与 pyrvinium 敏感性方向一致，但单独抑制 ERK 或 STAT3 没有复现，不能据此把该通路定为人体干预靶点。

## 06｜SBS17 为什么不像普通的年龄累积噪音

20 对 IM–normal WGS 样本中，作者识别到 SBS1、SBS5/40、SBS17 和 SBS18。SBS17 在正常胃中并不典型，却出现在 IM 和胃癌中；映射到 1,095 个胃窦 IM 后，287 个样本（26.2%）可检测到 SBS17。

SBS17 在最晚复制区域富集 14.5 倍，而且与吸烟相关，却没有随年龄显著增加。类器官中的 OXPHOS、氧耗和 8-oxo-dG 结果把它与氧化损伤联系起来，但这些实验仍不能证明 OXPHOS 直接制造了 SBS17。

![Fig. 4：SBS17、复制时序与氧化损伤](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig4-page11.png)

简明图注：Fig. 4 先在 20 对 IM–normal WGS 中识别突变签名，再映射到 1,095 个胃窦 IM，其中 287 个检出 SBS17；它在最晚复制区富集 14.5 倍，并与 IM 类器官的 OXPHOS/氧化损伤读出同向。后者仍是关联证据，不能证明 OXPHOS 直接产生 SBS17。

甲基化数据给出了另一层背景。14 名韩国患者的 38 份正常、异型增生和早期胃癌样本中，CIN/MSI 相关病灶出现广泛低甲基化：受检 CpG 中 6,741,487 个（35.7%）低甲基化，而 326,646 个（1.7%）高甲基化；原文称 SBS17 在这些低甲基化区域的 specificity 为 75.7%。这里仍是区域重叠，不能证明低甲基化先造成 SBS17。

## 07｜血液里的克隆能增加多少风险分层信息

作者在 1,067 名受试者中识别到 286 个已报道的克隆性造血（CH）相关基因突变，涉及 225 人，主要 driver 为 DNMT3A、TET2、ASXL1 和 PPM1D。

临床关联分析纳入 765 名 OLGIM II–IV 期受试者，其中 43 人有异型增生、26 人有 EGN。当 CH 变异等位基因频率超过 5% 时，high CH 在多变量分析中仍与 EGN 相关（P = 6.4 × 10^-3）。只使用 OLGIM、年龄和性别的模型 AUC 为 0.72；加入 mutation count、ARID1A mutation 和 high CH 后，AUC 提高到 0.773。

在有较长期随访的 GCEP1000 子集中，312 人只有 9 例 EGN，AUC 从 0.671 提高到 0.811。增量很明显，但事件数很少，而且没有独立外部队列验证，不能把这组 AUC 当作现成的临床工具。

![Fig. 5：CH driver、临床关联与风险模型](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig5-page14.png)

简明图注：Fig. 5 在 1,067 名受试者中描绘 CH，风险模型使用 765 人（43 例异型增生、26 例 EGN），并比较临床基线模型与加入 mutation count、ARID1A mutation、high CH 后的模型；AUC 由 0.72 升至 0.773，但事件少且没有独立外部验证。

## 08｜血液里的克隆为什么会连接到胃黏膜

CH 原本主要被视为血液系统老化现象。这篇论文更进一步，尝试把它连接到胃黏膜免疫和微生物生态。

高 CH 与 PIGR truncating mutation 共现（OR = 2.8，P = 0.017）。PIGR 是上皮细胞把 polymeric IgA 转运到黏膜表面的受体；这个关联提示黏膜屏障可能参与其中，但论文没有证明 CH 先造成 PIGR 突变。

数据方向与这个模型一致。scRNA-seq 比较 3 个 CH-high 与 10 个 CH-low IM，bulk RNA-seq 又比较 20 个 high CH 与 94 个 non/low CH IM；两层数据都指向 IgA+ plasma cells 和 mature T cells 增多，Streptococcus、Neisseria、Gemella、Fusobacterium 等口腔来源菌属也更丰富。

FISH 和 Stereo-seq 使用的不是 IM，而是胃癌组织。4 例胃癌的 Stereo-seq 中，2 例检出 Streptococcus 空间簇；其中 1 例与 CXCL8 高表达区域重叠，另 1 例与肠型上皮和 IgA plasma-cell signatures 重叠。这只能为机制模型提供探索性支持。

![Fig. 6：CH、PIGR、IgA 与口腔菌的关联模型](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig6-page16.png)

简明图注：Fig. 6 的单细胞比较为 3 个 CH-high 对 10 个 CH-low IM，bulk 比较为 20 个 high CH 对 94 个 non/low CH IM；FISH 和 Stereo-seq 则来自 4 例胃癌，只有 2 例检出 Streptococcus 空间簇。这些结果支持横断面关联和机制线索，不能证明 CH 先造成黏膜屏障与微生物改变。

但需要强调：共现、免疫组成和空间重叠构成的是一条机制线索，不是完整因果链。论文尚未证明 CH 先导致 PIGR 改变，再导致口腔菌定植并最终推动胃癌。

## 09｜这项研究真正改变了哪一步

胃肠化生过去常被当作一个静态病理标签。这项研究把它重新描述为一个由多层横断面证据刻画的演化状态：上皮细胞积累 driver 和 mutational signatures，部分患者同时出现 CH，并伴随不同的黏膜免疫与微生物特征。

近期最现实的价值不是用某一个 marker 取代胃镜，而是为前瞻风险模型指定候选变量。ARID1A truncation、mutation burden 和 high CH 是否真能改变随访强度，仍要在独立、事件数充足的纵向队列中重新训练、校准和验证。

KRAS/MAPK-altered IM 和 pyrvinium 类器官结果也提供了干预线索，但距离人体癌前干预还有很长距离。选择性、毒性、体内可达性和真实预防效果都尚未建立。

## 10｜这些结果仍需要冷静看待

首先，跨国家样本很多，但长期进展事件主要依赖新加坡队列。其他地区不少结局只是基线观察；总体模型只有 26 例 EGN，GCEP1000 子集只有 9 例，而且没有独立外部验证，因此“预测未来进展”的证据没有样本总数看起来那么强。

其次，高深度靶向 panel 以深度换广度。它适合捕捉低 VAF 克隆，却会遗漏 panel 外 driver、结构变异和非编码调控改变。

第三，SBS17、低甲基化与 OXPHOS 的关系仍以相关和区域重叠为主。pyrvinium 依赖药理抑制，缺少关键通路的遗传扰动；类器官选择性也不能直接转化为临床预防建议。

第四，微生物分析容易受到低丰度 reads、污染和反向因果影响。靶向 panel 本来并非为非 Hp 菌检测而设计；FISH、单细胞和空间数据虽提供多模态支持，但样本量有限，而且原位/空间验证来自胃癌组织。CH–PIGR–IgA–口腔菌这条链仍需要前瞻性队列和扰动实验。

最后，本地 PDF 不含 Supplementary Figures、Supplementary Tables S1–S14 或 Source Data；MSKCC 对照总人数在 Results/Fig. 5 中为 24,146，在 Methods 中为 24,126；Fig. 5A 按 1,067 名受试者，Fig. 5C 按 1,095 份样本（234 + 861），主 PDF 无法核对样本—受试者映射。这些问题不改变主要结论方向，但限制精确复现与分层解释。

## 11｜对我们的研究有什么可借鉴

如果要迁移到胃癌精准预防队列，可以把病理分层、高深度上皮 mutation panel、外周血 CH、吸烟与 Hp 暴露、口腔/胃微生物组和长期 EGN 终点放在同一设计中。

风险模型必须保留 OLGIM 等临床基线，再检验 ARID1A truncation、SBS17 exposure、mutation burden 和 high CH 能带来多少增量预测，而不是只报告单变量显著性。

机制研究则可以从 CH driver 分层开始。TET2、DNMT3A 和 ASXL1 不一定对应同一种黏膜炎症程序，需要用配套单细胞、空间转录组、IgA repertoire 和微生物组逐一验证。

---

## 技术附录

以下内容保留论文基本信息、完整主图说明、Results/Methods 证据、复现参数和证据边界。

### 基本信息

- 原文题名：Mutational Signatures and Clonal Hematopoiesis in Intestinal Metaplasia across Countries with Varying Stomach Cancer Incidence
- 期刊：Cancer Discovery 16, 497-520
- 年份：2026
- DOI：10.1158/2159-8290.CD-25-0778
- 第一作者：Kie Kyon Huang、Takeshi Hagihara
- 通讯作者：Patrick Tan、Khay Guan Yeoh
- 研究领域：胃癌癌前病变、胃肠化生、体细胞突变、突变签名、克隆性造血、微生物组、精准预防
- 关键词：intestinal metaplasia、gastric cancer、Correa cascade、Helicobacter pylori、SBS17、ARID1A、KRAS/MAPK、PIGR、clonal hematopoiesis、Streptococcus anginosus
- 数据来源：EGA `EGAD50000001538`（EM-seq）、`EGAD50000001539`（WGS）、`EGAD50000001540`（targeted sequencing）、`EGAD50000002010`（transcriptome）；GCEP1000 为 `EGAD00001010129`（targeted panel）、`EGAD00001010131`（bulk RNA-seq）、`EGAD00001010157`（WGS）、`EGAD00001010166`（scRNA-seq），均需申请访问（`P022.S0029–P022.S0033`）。
- 代码来源：主 PDF 未报告独立代码仓库；Methods 仅给出所用工具、版本或项目链接。
- 图像截取说明：已将主文 Fig. 1-7 所在页渲染为图片，位于 `assets/gastric-cancer/2026-im-mutational-signatures-ch/`。多页图按页面拆分显示。
- 本地 PDF：`pdfs/processed/intestinal-metaplasia-mutational-signatures-ch-2025.pdf`
- 本地 PDF SHA-256：`e788d7ec5dd8c25a19faeeea4fcc83b0ed10c418c3fbb1a8fe256acdf5a5c4e7`
- LLM pack：`tmp/im-mutational-signatures-ch-llm-pack.md`
- Manifest：`tmp/im-mutational-signatures-ch-manifest.json`

### PDF 解析质量与覆盖审计

- 抽取方式：使用 `scripts/build_pdf_llm_pack.py`，PyMuPDF 引擎。
- 总体覆盖：24 页、1,164 个句子 ID；1,164/1,164 已按 title/introduction、Results、Discussion、Methods、数据可用性、披露/作者贡献和 References 分类，未覆盖 ID：无。
- 主 Results：按论文版面校正为 `P003.S0015–P016.S0015`，521/521 个 ID。自动标签只正确识别 165 个；另有 356 个因跨页图注和双栏顺序被误标为 `supplementary`。
- 主 Methods：按原文 Methods 标题校正为 `P018.S0004–P022.S0028`，226/226 个 ID。自动标签只正确识别 115 个；另有 111 个在第 20–22 页被误标为 `supplementary`。数据可用性另覆盖 `P022.S0029–P022.S0033` 的 5/5 个 ID。
- Discussion：`P016.S0016–P018.S0003`，61/61 个 ID；其中作者明确列出随访、panel、药理扰动、SBS17 因果、微生物检测以及小规模单细胞/空间分析六类限制。
- 版面问题：图页 `P004`、`P006`、`P008`、`P010`、`P013`、`P014`、`P017` 混入坐标轴、页码和跨栏图注；`P007.S0043–P009.S0002`、`P011.S0042–P012.S0005`、`P012.S0052–P015.S0002`、`P017.S0030–P018.S0003` 跨图页或跨页续接。本文只把可与正文/图注相互核对的图内数字作为证据。
- 缺失材料：本地 PDF 不含 Supplementary Figures、Supplementary Tables S1–S14 或其 Source Data。正文引用这些材料时，本笔记只保留主文可验证的结论和缺口，不补写无法核对的分层明细。
- 低置信点：图表 OCR 中有拆词与希腊字母噪音；Methods 的 `P019.S0010–P019.S0012` 写作 “Student t test (two-way)”，原意可能是 two-tailed，但不能静默修正；MSKCC 对照总人数在 Results 为 24,146、Methods 为 24,126，见下文冲突记录。

---

### 本论文主图与完整 panel 注释

| 原文图表 | 完整 panel 注释 | 样本、比较与统计 | 图像文件 | 正文位置 |
|---|---|---|---|---|
| Fig. 1 | A：六个国家/地区的样本、胃癌年龄标化率及测序/组织学 Hp 阳性率；B：Hp-positive 样本系统发育；C：日本/韩国 clade 与新加坡 clade 的 CagA E106D、R109K、N228H；D：变异在 cagA 上的位置；E：CagA–ASPP2 结构模型；F：两类 CagA 与野生型/不结合 ASPP2 的 reciprocal co-IP。 | 全图队列 1,680 份组织（1,582 IM、98 normal）；高丰度 Hp 比较为韩国 24/106、日本 2/33、新加坡近期 3/218；co-IP 四次独立重复。来源 `P003.S0030–P005.S0018`、图注 `P004.S0018–P004.S0034`。 | `fig1-page4.png` | [01](#01｜只看幽门螺杆菌，为什么还不够) |
| Fig. 2 | A：1,095 个胃窦 IM 的 36-gene oncoprint 与 EGN forest plot；B：SOX9、ARID1A 等在不同人群的 lollipop/frequency；C：国际队列和 TransGCEP1000 中 ARID1A truncation 与 EGN。 | Chinese `n = 909` 对 Japanese/Korean `n = 142`；ARID1A 合并 OR 6.2、P = 1.5 × 10^-3；Fig. 2 另显示分队列 OR。来源 `P005.S0019–P006.S0030`。 | `fig2-page6.png`, `fig2-page7.png` | [04](#04｜哪些上皮-driver-真正关联早期胃肿瘤) |
| Fig. 3 | A：KRAS、BRAF、MAP2K1 gain-of-function 与 MAP2K4、MAP3K1、NF1 loss-of-function；B：KRAS/MAPK-mutant bulk RNA GSEA；C：scRNA epithelial type、cell cycle 与 KRAS–ERK score；D：CDX2；E：胃/肠谱系表达；F：severe 对 mild IM organoid；G：pyrvinium 活力。 | Bulk 为 10 个 mutant 对 94 个无可检出改变；down-sampling 1,000 次；organoid 为 6 IM 对 4 normal，Fig. 3G 为 1 μmol/L、72 h、每组 4 个 biological replicates，linear mixed-effects P < 0.0005。来源 `P007.S0001–P009.S0007`、图注 `P008.S0002–P008.S0008` 与 `P009.S0037–P009.S0046`。 | `fig3-page8.png`, `fig3-page9.png` | [05](#05｜kras–mapk-改变能否提供干预线索) |
| Fig. 4 | A：20 对 IM–normal WGS 的四类 SBS；B：79 个正常胃、20 个 IM、122 个胃癌；C：各 signature VAF；D：复制时序；E：6 IM 对 4 normal organoid 的 OXPHOS；F：OCR；G：8-oxo-dG；H：年龄和吸烟。 | SBS17 在最晚复制区 14.5×；OCR 的 basal/maximal P = 0.035/0.015；8-oxo-dG 每个 organoid 六次 technical replicates，按个体内 mean ± 1.5 SD 去异常；targeted 映射为 287/1,095。来源 `P009.S0008–P011.S0019`、图注 `P010.S0047–P010.S0057` 与 `P011.S0043–P011.S0052`。 | `fig4-page10.png`, `fig4-page11.png` | [06](#06｜sbs17-为什么不像普通的年龄累积噪音) |
| Fig. 5 | A：1,067 名受试者的 CH oncoprint；B：DNMT3A、TET2、ASXL1、PPM1D 与 MSKCC 对照；C：CH 与年龄/IM mutation count；D：CH gene 与吸烟；E：dysplasia/EGN logistic regression。 | 风险模型 `n = 765`（43 dysplasia、26 EGN）；GCEP1000 `n = 312`（20 dysplasia、9 EGN）。Fig. 5C 用 234 个 CHIP-positive 与 861 个 CHIP-negative IM samples，与 1,067 名受试者口径不同。来源 `P012.S0013–P015.S0002`、图注 `P013.S0031–P013.S0037`。 | `fig5-page13.png`, `fig5-page14.png` | [07](#07｜血液里的克隆能增加多少风险分层信息) |
| Fig. 6 | A：high CH 关联的 IM drivers；B：PIGR mutation type；C：PIGR 与 CH genes；D：作者提出的屏障—微生物—炎症模型；E：scRNA immune composition；F：bulk deconvolution 与 bacterial/human reads；G：菌属差异；H：Streptococcus/S. anginosus FISH；I：Streptococcus 与 CXCL8 空间重叠。 | scRNA 为 3 high 对 10 low CH；bulk 为 20 对 94，另做 1,000 次平衡下采样；Fig. 6G 初始 `n = 104`，10 个 bacterial reads <0.02% 样本被排除；H–I 是胃癌组织，Stereo-seq 4 例中 2 例检出空间簇、图中展示其中 1 例。来源 `P015.S0003–P016.S0015`、图注 `P014.S0023–P014.S0034` 与 `P015.S0040–P015.S0048`。 | `fig6-page14.png`, `fig6-page15.png`, `fig6-page16.png` | [08](#08｜血液里的克隆为什么会连接到胃黏膜) |
| Fig. 7 | 在 Correa cascade 上整合 Hp 菌株、上皮 driver/SBS、CH、免疫和微生物，并标出风险分层、pyrvinium 与抗菌等转化设想。 | 概念总结图，不是新增实验；蓝框中的干预均未在患者中验证。来源 `P017.S0001–P017.S0033`。 | `fig7-page17.png` | [09](#09｜这项研究真正改变了哪一步) |

### 生物学故事前情

胃肠化生是 Correa cascade 中连接慢性萎缩性胃炎和异型增生/胃癌的关键癌前阶段。传统上，领域把风险主要放在幽门螺杆菌感染、OLGIM 分期、家族史、吸烟饮酒等临床流行病学因素上；但这些指标很难解释为什么大多数 IM 不进展，而少数病灶会跨过异型增生和早期癌的门槛。

这篇文章把 IM 当作一个正在演化的生态系统，而不是单纯的组织学状态。作者同时看三类事件：上皮细胞内的 driver mutations 和 mutational signatures，非上皮血液系统的 clonal hematopoiesis，以及黏膜免疫-微生物互作。它的核心问题是：不同胃癌风险国家中的 IM 是否已经带有可解释地区发病率差异和未来进展风险的分子轨迹？

读这篇文章要抓住两条主线。第一条是上皮内事件：ARID1A、SOX9、KRAS/MAPK、SBS17 等改变如何标记 IM 的克隆演化和增殖状态。第二条是非上皮事件：CH 是否通过改变免疫炎症状态、PIGR/IgA 屏障和口腔来源细菌定植，推动 IM 向后期 Correa cascade 进展。

### 重要缩写表

| 缩写 | 中文含义 | 本文语境中的具体指代 | 阅读时注意 |
|---|---|---|---|
| IM | intestinal metaplasia，胃肠化生 | 胃癌前病变，主要分析对象 | 不是所有 IM 都会进展为胃癌 |
| Hp | Helicobacter pylori，幽门螺杆菌 | 通过靶向 panel 中 6 个 Hp 基因 coverage 推断感染/菌株变异 | IM 形成后 Hp 可下降，因此阴性不等于从未感染 |
| EGN | early gastric neoplasia | 高级别异型增生或早期胃癌 | 本文风险预测的关键终点之一 |
| OLGIM | Operative Link on Gastric Intestinal Metaplasia Assessment | 基于 IM 范围和严重度的临床分期 | 仍是临床风险分层基础，分子指标是在其上加信息 |
| VAF | variant allele frequency | 突变等位基因频率，反映克隆比例和测序检测阈值 | IM 突变 VAF 很低，所以需要高深度测序 |
| WGS | whole-genome sequencing | 20 对 IM-normal 用于突变签名和全基因组分布 | 深度约 60x，不足以完整捕捉低 VAF driver |
| SBS | single-base substitution signature | 单碱基替换突变签名 | SBS17 是本文最重要的 IM 特异性签名 |
| CH | clonal hematopoiesis | 血液/唾液正常样本中的造血克隆扩增突变 | 本文作为非上皮风险因子，而非血液肿瘤诊断 |
| CHIP | clonal hematopoiesis of indeterminate potential | 文中按 VAF > 2% 定义的 CH 事件 | 高 CH 另按 VAF > 5% 分层 |
| PIGR | polymeric immunoglobulin receptor | 黏膜上皮转运 IgA 的受体，truncating mutation 与高 CH 共现 | PIGR 突变提示黏膜免疫屏障受损，但因果仍待验证 |
| Sa | Streptococcus anginosus | 文章关注的口腔来源细菌之一 | FISH 和 Stereo-seq 在胃癌组织中做探索性验证 |
| OXPHOS | oxidative phosphorylation | IM organoid 中增强的线粒体氧化磷酸化 | 与 SBS17/氧化损伤关联主要是相关性证据 |

### 论文详细解读

#### 研究问题与科学背景

胃癌发病率在国家和地区之间差异很大，日本和韩国等高风险地区明显高于新加坡、北美等中低风险地区。Hp 是最强风险因素之一，但仅用 Hp 感染不能完全解释地区差异和 IM 个体间进展差异。IM 患者总体有更高胃癌风险，但绝对年进展风险较低，临床上不可能对所有 IM 患者进行同等强度随访。

作者提出的科学瓶颈是：IM 阶段是否已经积累了足够的遗传、表观遗传、突变过程和免疫-微生物变化，可以解释胃癌风险异质性，并用于识别真正高危的 IM 患者。

#### 研究设计与数据结构

本文用 277 个 human genes 和 6 个 Hp genes 的高深度靶向 DNA sequencing 分析 1,582 个 IM 样本，平均深度 1,108x。新近招募队列包括新加坡 218、韩国 106、香港 62、美国 36、日本 33、台湾 8 个 antral IM，并有配对 germline；同时加入既往 TransGCEP1000 新加坡 IM 样本 1,119 个和正常胃样本 98 个。

作者还加入多个补充数据模态：20 个 IM-normal 配对样本做 WGS，平均覆盖 60.5x；韩国 14 名患者的 matched normal、dysplasia、early gastric cancer 共 38 个样本做 EM-seq；部分样本有 bulk RNA-seq、scRNA-seq、IM microbiome、saliva microbiome、organoid 和 Stereo-seq 数据。整体设计不是单一组学发现，而是用靶向深测序作为主轴，再用 WGS、转录组、表观组、类器官和微生物空间证据补强机制解释。

#### 方法速览与分析框架

靶向测序用于捕捉低 VAF IM 突变。作者用统一 pipeline 调用 somatic mutations，并说明 WGS 或模拟 100x WES 只能恢复一小部分低频突变，因此高深度 panel 是本文发现 IM driver 的技术前提。

driver gene 发现用 IntOGen pipeline，整合 7 个互补算法并做组合 q 值。突变签名分析先在 20 个 WGS IM 样本上用 SigProfilerAssignment 推断 SBS1、SBS5/40、SBS17、SBS18，再把签名映射到 1,095 个 antrum IM 靶向数据中。CH 调用采用“反向 tumor-normal”思路：把 blood/saliva 当作待检测对象，IM 当作对照，筛选血液/唾液 VAF 更高的造血克隆突变。

临床风险部分用 logistic regression，把年龄、性别、OLGIM、mutation count、ARID1A truncation、CH/高 CH 等变量与 dysplasia 或 EGN 关联。机制部分则通过 bulk/scRNA-seq deconvolution、PathSeq/lefser 微生物分析、FISH、IHC 和 Stereo-seq 连接 CH、PIGR、IgA+ plasma cells 和口腔菌。

#### 原文结果完整梳理

##### Data Collection

来源范围：`P003.S0015–P003.S0029`。

作者首先建立跨国家 IM 图谱：1,582 个 IM 加 98 个正常胃样本，主数据为高深度 targeted DNA-seq。最近收集的 antrum IM 来自 6 个国家/地区，并结合新加坡早期队列。这个设计使文章能同时比较地理风险、Hp、driver genes、SBS signatures 和 CH。

关键技术点是测序深度。IM 里许多 somatic mutations 的 VAF 很低，若使用常规 WES/WGS 深度会大量漏检。作者后续结果表明，WGS 只能恢复靶向 panel 检出的 17.5% somatic mutations；模拟 100x WES 只能恢复 15.5% somatic mutations 和 15.1% driver protein-altering mutations。

##### Geographic Patterns of Hp Strains and Infection

来源范围：`P003.S0030–P005.S0018`（含 Fig. 1 全 panel 图注与图页文本）。

![Fig. 1：跨国家 IM 队列与 Hp 菌株差异](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig1-page4.png)

中文图注（基于原文图注）：Fig. 1 展示 6 个国家/地区 IM 样本分布、测序和组织学 Hp 阳性率、Hp-positive 样本的系统发育结构、CagA 变异位点、CagA-ASPP2 结构模型和免疫共沉淀验证。核心信息是高风险日本/韩国 Hp strain 与新加坡 strain 在 CagA N 端变异上分离，并且高风险地区 CagA variant 与 ASPP2 结合更强。

Hp 阳性率在高风险地区更高。韩国近期 IM 中高丰度 Hp 为 24/106，日本为 2/33，而近期新加坡仅 3/218；香港、美国、台湾近期样本未检测到高丰度 Hp。既往新加坡 2000-2010 队列 Hp 水平更高，提示根除策略和采样年代会影响观察到的 Hp burden。

Hp 变异也有地区差异。作者在 Hp-positive 样本中看到日本/韩国与新加坡菌株的系统发育分离，并把差异定位到 cagA 的 E106D、R109K、N228H。高风险地区 CagA variant 与 ASPP2 结合更强，而东南亚常见 variant 结合减弱。作者据此提出：不仅 Hp 是否存在重要，Hp virulence gene 的遗传多样性也可能影响 Correa cascade 起点和地区胃癌风险。

##### Driver Gene Landscape of Trans-geographic IM Samples

来源范围：`P005.S0019–P006.S0030`（含 Fig. 2 全 panel 图注与图页文本）。

![Fig. 2a：IM driver gene landscape](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig2-page6.png)

![Fig. 2b-c：地区差异和 ARID1A 与 EGN](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig2-page7.png)

中文图注（基于原文图注）：Fig. 2 展示 36 个代表性 driver genes 的 oncoprint、不同人群/地区的关键 driver mutation rate，以及 ARID1A truncating mutations 与 EGN 的关联。图中重点是中国人群中 SOX9 truncation 频率高，而日本/韩国高风险人群中 ARID1A、ARID2、ERBB3 等更常见。

IntOGen 在 IM 中识别 47 个显著突变基因，共 2,100 个 driver mutations，其中 25 个此前未在 IM 中报告。47 个 driver genes 中 37 个也出现在正常胃、TCGA pan-GI cancer 或 IntOGen 胃癌 driver 资源中，说明这些基因与胃上皮癌变相关性较强。

antrum IM 的平均 somatic mutation count 为 23，平均 VAF 2.9%，中位 VAF 1.7%。日本/韩国样本突变率高于中国人群。SOX9 mutation 尤其在 Chinese populations 中更常见，909 个样本中 114 个有 SOX9 mutations，其中 94 个是 truncating mutations；而高风险日本/韩国人群中 ARID1A、ARID2、ERBB3、KMT2D、KDM6A、CREBBP、PREX2 更常见。

最有转化价值的是 ARID1A。跨地区合并分析显示，ARID1A truncating mutations 与 concurrent 或 eventual EGN 关联，OR 6.2，P = 1.5e-3。作者将其解释为 SWI/SNF 失活可能促进 enhancer accessibility、lineage fidelity 和 epithelial plasticity 改变，从而提高 IM 向 neoplasia 转化的可能。

##### KRAS-MAPK mutations in IM

来源范围：`P007.S0001–P009.S0007`（Fig. 3 跨第 8–9 页；图注分别为 `P008.S0002–P008.S0008` 与 `P009.S0037–P009.S0046`）。

![Fig. 3a-b：KRAS/MAPK driver 与通路激活](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig3-page8.png)

![Fig. 3c-g：scRNA-seq、IM organoid 和 pyrvinium](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig3-page9.png)

中文图注（基于原文图注）：Fig. 3 展示 KRAS、BRAF、MAP2K1 的 gain-of-function 以及 MAP2K4、MAP3K1、NF1 的 loss-of-function 改变；bulk RNA-seq 证明 KRAS/MAPK-mutated IM 激活 KRAS-ERK signatures；scRNA-seq 显示 cycling intestinal stem/TA cells KRAS-ERK 分数更高；IM organoid 通过 CDX2 和转录组确认，并对 pyrvinium 更敏感。

KRAS/MAPK 通路改变存在于一部分 IM 中。作者观察到 KRASG12D、BRAFD594G、MAP2K1F53L 等激活性突变，以及 MAP2K4、MAP3K1、NF1 等负调控因子的失活。104 个同时有 DNA 和 bulk RNA-seq 的 IM 样本中，10 个带 KRAS/MAPK driver alterations，这些样本显著上调 KRAS、ERK 和 KRAS-ERK intersected signatures；下采样 1,000 次后结果仍稳定。

单细胞分析把通路激活定位到增殖相关细胞状态。KRAS-ERK signature 在 gastric stem cells 中较高，也在 cycling intestinal stem cells 和 transit-amplifying cells 中显著升高。作者提出 KRAS-ERK 可能促进静息 IM stem cells 进入细胞周期，推动肠型谱系扩增。

类器官实验提供药物干预线索。作者建立 6 个 IM 和 4 个正常胃 organoids，IM organoids 表达 CDX2、REG4、FABP1、CDX1 等肠型标志。severe IM organoids 的 KRAS-ERK signaling 更高；在 Fig. 3G 的 1 μmol/L、72 小时实验中，每组 4 个 biological replicates，IM organoid viability 比正常胃 organoid 降得更多（linear mixed-effects P < 0.0005），100 nmol/L pyrvinium 也降低 IM 的 colony-forming ability。单独 ERK 或 STAT3 inhibition 没有复现同等选择性，说明 pyrvinium 作用可能不只是单一路径抑制。

##### SBS17 Is an IM-associated Mutational Signature

来源范围：`P009.S0008–P011.S0019`（Fig. 4 跨第 10–11 页；图注分别为 `P010.S0047–P010.S0057` 与 `P011.S0043–P011.S0052`）。

![Fig. 4a-e：IM mutational signatures 与复制时序](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig4-page10.png)

![Fig. 4f-h：OXPHOS、8-oxo-dG、年龄和吸烟](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig4-page11.png)

中文图注（基于原文图注）：Fig. 4 展示 20 个 IM WGS 样本的 SBS1、SBS5/40、SBS17、SBS18 组成；与正常胃和胃癌比较；SBS17 的 VAF 偏低；SBS17 在 late-replicating regions 高度富集；IM organoids 中 OXPHOS、OCR 和 8-oxo-dG 增强；SBS17 与吸烟相关而不随年龄显著增加。

20 个 IM-normal WGS 样本中识别 4 类主导 signature：SBS1、SBS5/40、SBS17、SBS18。SBS1、SBS5/40、SBS18 也出现在正常胃，SBS17 则在 IM 和胃癌中出现但正常胃中不典型，提示它可能是 IM 阶段新出现的 mutagenic process。SBS17 mutations 的 VAF 低于其他 SBS mutations，支持其更多代表晚期或 subclonal events。

SBS17 的基因组分布有鲜明特征。按 replication timing 四分位分层后，SBS1、SBS5/40、SBS18 在 late-replicating regions 仅中等升高，而 SBS17 在最晚复制区域富集 14.5 倍。作者将其与 OXPHOS、氧化损伤、8-oxo-dG 和 nucleotide pool damage 联系起来。IM organoids 的 OXPHOS pathway、basal/maximal OCR 和 8-oxo-dG 水平均高于正常 organoids；DCA 增强 OXPHOS 后可提高 ROS 和 DNA damage，但作者明确承认这还不能证明 OXPHOS 直接造成 SBS17。

映射到 1,095 个 antrum IM 靶向数据后，SBS5/40 和 SBS1 几乎普遍存在，SBS18 和 SBS17 分别在约 28.9% 和 26.2% 样本中可检测。高风险国家 IM 的所有 signature mutation rate 均更高，其中 SBS17 enrichment 更明显。SBS1、SBS5/40、SBS18 与年龄相关，SBS17 不随年龄显著相关，但与吸烟显著相关。这个结果把 SBS17 从“年龄累积噪音”中区分出来，使其成为潜在进展风险或暴露相关 biomarker。

##### Hypomethylation in Developing Gastric Cancer

来源范围：`P011.S0020–P012.S0005`。

作者对韩国 14 名患者的 38 份 matched normal、dysplasia 和 early gastric cancer 做 EM-seq。PCA/层次聚类得到两组：一组以 CIN/MSI 病灶为主（14 份中的 10 份），另一组以缺少 CIN/MSI/EBV 特征的 normal 或病灶为主（24 份中的 22 份；Fisher P = 1.1 × 10^-4）。

CIN+/MSI+ 组相对另一组有 6,741,487 个低甲基化 CpG（35.7%）和 326,646 个高甲基化 CpG（1.7%）；按 1 kb 区域分析则为 750,775 个低甲基化区域（38.4%）和 11,273 个高甲基化区域（0.57%），阈值均为 q < 0.001、甲基化差异 >10%。原文把 SBS17 在这些低甲基化区域中的 specificity 报为 75.7%，并称它在晚复制、低甲基化区域进一步增加；本地 PDF 没有给出该 specificity 的独立公式。它支持区域重叠，不证明低甲基化、晚复制或 OXPHOS 中任何一项单独造成 SBS17。

##### Germline variants associated with dysplasia and EGN

来源范围：`P012.S0006–P012.S0012`。

在 47 个 somatic driver genes 中，44 个也观察到 protein-altering germline variants；其中 8 个 ClinVar pathogenic/likely pathogenic variants 涉及 11 人。BCORL1 同时出现 germline 与 somatic variants 时，与 EGN（OR = 3.72，P = 0.033）和 dysplasia（OR = 3.97，P = 0.0048）相关；BCOR 和 DDX3X 的双重改变也分别与 dysplasia 相关（OR = 2.71、4.00；P = 0.039、0.029）。这些事件稀少且来自探索性列联分析，不能当作已验证的遗传风险标志。

##### Clonal Hematopoiesis in IM Samples

来源范围：`P012.S0013–P015.S0002`（Fig. 5 图页插在正文续句之间）。

![Fig. 5a-d：IM 患者 CH driver 与年龄/吸烟](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig5-page13.png)

![Fig. 5e：CH 与 dysplasia/EGN 风险模型](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig5-page14.png)

中文图注（基于原文图注）：Fig. 5 展示 1,067 名 IM subject 中 CH mutations 的分布，DNMT3A、TET2、ASXL1、PPM1D 等 CH genes 的突变位置与 MSKCC pan-cancer CH 数据对照，CH carriers 年龄更大且 IM somatic mutation rate 更高，ASXL1 mutation 与吸烟相关；logistic regression 显示 high CH 与 dysplasia/EGN 风险相关。

作者在 1,067 名 IM subjects 中识别 286 个 reported CH gene mutations，分布于 225 人。显著 CH driver genes 为 DNMT3A、TET2、ASXL1、PPM1D，突变谱与既往 MSK-IMPACT 大队列中的 CH 规律一致，例如 DNMT3A R882 missense、TET2/ASXL1 truncation、PPM1D 3' 区域 truncation。

CH carriers 年龄更大，IM somatic mutation rate 更高。ASXL1 mutation 在吸烟者中更常见，符合 CH 与烟草暴露关系的既往认识。关键临床分析中，作者把 CH 分为 CHIP VAF > 2% 和 high CH VAF > 5%。在 765 名 unique IM subjects 中，CHIP、高 CH、mutation rate、ARID1A truncation、年龄、男性、OLGIM stage III/IV 均与 dysplasia 有关；多变量中 high CH、男性、OLGIM stage III 独立关联 dysplasia。

对 EGN 终点，高 CH 和 ARID1A truncation 在多变量模型中仍显著。765 名受试者中只有 26 例 EGN；GCEP1000 长期随访子集为 312 人、9 例 EGN。风险模型中，临床变量 OLGIM、年龄、性别的 AUC 为 0.72；加入 mutation count、ARID1A mutation 和 high CH 后 AUC 升至 0.773。GCEP1000 子集中，AUC 从 0.671 升至 0.811。这个结果支持把 CH 作为候选风险变量，但事件数少且缺少外部验证，尚不能称为可部署的血液预测指标。

##### CH expansions are associated with altered IM Microbiome-Immune Landscapes

来源范围：`P015.S0003–P016.S0015`（Fig. 6 全 panel 图注分别为 `P014.S0023–P014.S0034` 与 `P015.S0040–P015.S0048`）。

![Fig. 6a-d：CH、PIGR 和黏膜免疫模型](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig6-page14.png)

![Fig. 6e-g：CH-high IM 的免疫和细菌组成](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig6-page15.png)

![Fig. 6h-i：Streptococcus/Sa FISH 和空间炎症](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig6-page16.png)

中文图注（基于原文图注）：Fig. 6 展示 high CH 与 IM driver genes 的共现，其中 PIGR truncating mutation 与 high CH 关联；PIGR 参与 IgA transcytosis；CH-high IM 中 IgA+ plasma cells 和 mature T cells 增加；口腔来源细菌如 Streptococcus、Neisseria、Gemella、Fusobacterium 增加；FISH 和 Stereo-seq 在胃癌组织中显示 Streptococcus/Sa 与 CXCL8 炎症区域空间重叠。

作者进一步问 CH 如何影响 IM 进展。driver gene 共现分析显示，高 CH 与 PIGR mutations 相关，特别是 PIGR truncating mutations；PIGR truncation 还与 TET2 CH mutation 共现。PIGR 是上皮细胞把 polymeric IgA 转运到黏膜表面的关键受体，因此 PIGR truncation 可以被理解为黏膜 IgA 屏障受损的线索。

微生物结果支持“屏障-口腔菌-炎症”的模型。IM 中 PIGR truncating mutation 与 Streptococcus abundance 升高有关，但与 Helicobacter 不显著相关。scRNA-seq 中 high CH IM 的 immune cell types 增多，主要由 IgA+ plasma cells 和 mature T cells 推动；bulk RNA-seq deconvolution 在 20 个 high CH 与 94 个 non/low CH IM 中复现 IgA+ plasma cells 和 mature T cells 升高。IgA+ plasma cell abundance 与 bacterial reads 相关，而与 human reads 不相关。

CH-high IM 中多个口腔来源菌属升高，包括 Streptococcus、Neisseria、Gemella、Actinomyces、Haemophilus、Porphyromonas、Fusobacterium。唾液 metagenomics 支持这些菌属可能来自口腔。作者进一步用 FISH 在胃癌组织中检测 Streptococcus anginosus。Stereo-seq 只做了 4 例胃癌组织：2 例检出 Streptococcus 空间簇，其中一例与 CXCL8 高表达区域重叠，另一例与肠型上皮/IgA plasma cell signatures 重叠。由于样本少、对象是胃癌而不是 IM，这部分更适合作为机制假说支持，而不是 IM 阶段的最终因果证明。

#### 作者结论与证据强度

![Fig. 7：Correa cascade 中的综合模型和转化机会](../../assets/gastric-cancer/2026-im-mutational-signatures-ch/fig7-page17.png)

作者已经较有力证明：跨国家 IM 队列中存在复发 driver genes，且部分 driver frequencies 具有地区差异；ARID1A truncation 与 EGN 相关；KRAS/MAPK-altered IM 具有通路激活和类器官药物敏感性；SBS17 是 IM 相对正常胃更特异的突变签名，且与 late replication、OXPHOS/氧化损伤和吸烟相关；high CH 在本队列内与 dysplasia/EGN 独立相关，并提高内部模型 AUC。

合理但仍需验证的是：CH 通过 PIGR、IgA 屏障、口腔菌定植和慢性炎症推动 IM 向胃癌进展。本文有共现、转录组、微生物、FISH 和空间组学证据，但关键因果链条仍缺少前瞻性大队列和实验扰动验证。

原文没有证明的是：SBS17 可单独作为临床进展预测指标，pyrvinium 可用于人体 IM 干预，或者针对非 Hp 口腔菌的抗菌策略能降低 IM 进展风险。这些都应视为转化机会，而非已成熟的临床建议。

### Results 证据覆盖审计

| 原文句子 ID | 忠实中文含义 | 读者正文对应 | 证据边界 |
|---|---|---|---|
| `P003.S0015–P003.S0029`（15/15） | 1,582 个 IM、98 个 normal、六地近期队列与 TransGCEP1000；20 对 WGS、14 人/38 份 EM-seq 及唾液微生物组。 | 02、03 | 不同分析的样本/受试者分母不同；Supplementary Table S1 的逐人明细不在本地 PDF。 |
| `P003.S0030–P005.S0018`（62/62） | Hp 检出、历史感染、地区系统发育、CagA 三个位点、AlphaFold 接触与 co-IP。 | 01 | Hp 丰度受根除年代和 IM 后生态改变影响；CagA–ASPP2 对地区风险的贡献仍是机制推断。 |
| `P005.S0019–P006.S0030`（52/52） | IntOGen 47 genes/2,100 drivers、独立 48 IM 验证、地区频率、ARID1A–EGN 与深度下采样。 | 03、04 | Panel 限定候选空间；ARID1A 是关联，不是经过外部纵向验证的预测标志。 |
| `P007.S0001–P009.S0007`（58/58） | KRAS/MAPK mutations、10 对 94 bulk GSEA、1,000 次下采样、scRNA cell states、6 对 4 organoids 与药物实验。 | 05 | Pyrvinium 不是单一路径特异抑制剂；药理和类器官结果不能替代遗传扰动或人体预防试验。 |
| `P009.S0008–P011.S0019`（115/115） | 20 对 WGS 的四类 SBS、克隆结构、14.5× late-replication、OXPHOS/OCR/8-oxo-dG/DCA、1,095 个 panel 映射及年龄/吸烟。 | 06 | 60× WGS 对小亚克隆灵敏度有限；SBS17、OXPHOS、吸烟和氧化损伤仍是关联链。 |
| `P011.S0020–P012.S0005`（38/38） | 14 人/38 份 EM-seq、CIN/MSI 分组、CpG/region 低甲基化以及 SBS17 与晚复制低甲基化区域重叠。 | 06 | 没有纵向顺序或扰动，不能确定甲基化与 SBS17 的因果方向。 |
| `P012.S0006–P015.S0002`（120/120） | Germline variants；CH calling 结果、年龄/吸烟、765 人临床模型、26 个 EGN 与 GCEP1000 风险分析；Fig. 5 图页。 | 07 | Germline 事件稀少；总体和长期子集 EGN 仅 26/9 例，AUC 没有独立外部验证。 |
| `P015.S0003–P016.S0015`（61/61） | High CH–PIGR、3 对 10 scRNA、20 对 94 bulk、口腔菌/唾液、Gram/IHC、FISH 与 4 例胃癌 Stereo-seq。 | 08 | 多数证据横断面；FISH/Stereo-seq 来自胃癌而非 IM，空间样本极少。 |

审计结论：主 Results 连续范围 `P003.S0015–P016.S0015` 的 521/521 个 ID 已逐段归账，未覆盖 ID：无。Manifest 自动标为 `results` 的 165 个 ID 均属主 Results；另有 356 个真实 Results ID 因图页、双栏和跨页续接被误标为 `supplementary`，已全部人工校正。

### 独立方法学详解

#### 研究对象、样本和数据结构

主队列为跨国家 IM 样本，包含新近招募的 antrum IM 和既往新加坡 GCEP1000 队列。样本类型包括 IM、正常胃、配对 germline、部分 dysplasia/early gastric cancer、唾液和胃癌组织。临床信息包括年龄、吸烟、IM severity、OLGIM stage、家族史、dysplasia 或 EGN 结局。

这个设计的优点是样本量大、地理来源多、靶向测序深度高；缺点是不同国家样本采集时间、随访长度和临床终点成熟度不一致。GCEP1000 有较长随访，国际样本多为基线记录，因此进展风险分析仍主要依赖有限终点数。

#### 实验流程和数据生成

靶向 panel 使用 Agilent SureSelect XT HS2，覆盖 277 个人类基因和 6 个 Hp 基因，NovaSeq PE150 测序。WGS 使用 NEBNext Ultra II DNA library prep，NovaSeq PE150，平均约 60x。EM-seq 用 NEBNext Enzymatic Methyl-seq，结合 lambda/pUC19 controls 做甲基化 QC。

转录组层面使用 bulk RNA-seq 和 scRNA-seq，并复用此前数据加新样本。organoid 实验从正常胃和 IM 建立类器官，用 CDX2 immunostaining 和 RNA-seq 证明 IM identity，随后做 pyrvinium、ERK inhibitor、STAT3 inhibitor 处理和 ATP/colony assays。微生物部分结合 targeted DNA-seq、bulk RNA-seq PathSeq、唾液 shotgun metagenomics、Gram stain、FISH 和 Stereo-seq。

#### 数据预处理和特征构建

DNA reads 对齐到 hs37d5，靶向测序用 molecular barcode 去重复，WGS 用 MarkDuplicates。germline mutation 用 HaplotypeCaller，somatic mutation 用 Mutect2。深测序 somatic calling 为提高敏感性调整 Mutect2 参数，并用 gnomAD、panel of normals、contamination 和 read orientation artifact filters 控制假阳性。最终 somatic variants 要求至少 5 条 variant-supporting reads 且 VAF >= 1%。

Hp status 由 6 个 Hp genes 的 coverage 推断，>=1x 进入系统发育分析。driver genes 用 IntOGen 从 somatic mutations 中寻找正选择信号。SBS signatures 用 WGS 先拟合 COSMIC signatures，再把 SBS1、SBS5/40、SBS17、SBS18 映射到 targeted sequencing。CH calling 反向使用 blood/saliva as tumor、IM as control，并要求 blood/saliva VAF >= 2%，且至少为 matched IM VAF 的 2 倍。

#### 统计学分析方法

Fisher exact test 用于二分类变量关联，例如 Hp positivity、CagA variants、driver mutation frequency、PIGR truncation 与 high CH 共现。其输入是 2x2 或类似列联表，估计 odds ratio 和 P value；适合稀疏突变事件，但不能处理多个混杂变量。

Wilcoxon test 用于比较非正态连续变量，例如 mutation count、signature exposure、bacterial abundance、immune cell abundance。它检验分布位置差异，但不直接估计可解释的绝对效应大小；多重比较时需要结合 FDR 或明确探索性解释。

Pearson/Spearman correlation 用于 signature exposure 与年龄、IgA+ plasma cells 与 bacterial reads 等连续变量关系。Pearson 假设线性关系，Spearman 更关注秩相关；相关性不能证明因果。

Logistic regression 用于 dysplasia/EGN 风险分析。输入包括临床变量和分子变量，输出 OR、P value 和多变量独立关联。本文策略是先单变量筛选，再多变量评估。需要注意 EGN 事件数有限，模型存在过拟合风险，AUC 提升应在外部队列验证。

Linear mixed-effects model 用于 organoid drug response/OCR 等实验，适合处理 biological replicates 和个体来源差异。GSEA/fgsea 用于判断 KRAS、ERK、OXPHOS 等 gene sets 是否在排序基因列表中系统富集，输出 NES 和 FDR。

#### 统计模型、机器学习模型或计算框架

IntOGen 是 driver discovery 框架，整合多个算法对突变频率、功能影响、聚集性和背景突变率进行正选择评估。它的优点是降低单一算法偏差；局限是候选基因受 panel 设计限制，不能发现 panel 外 driver。

SigProfilerAssignment 是突变签名分解工具，把每个突变按 trinucleotide context 分配到 COSMIC signatures。WGS 更适合签名发现，因为覆盖非编码区域；targeted panel 可做 signature projection，但对 SBS17/SBS18 这类偏 late-replicating noncoding regions 的 signature 敏感性不足。

CIBERSORTx 和 ESTIMATE 用于从 bulk RNA-seq 推断免疫成分。它们依赖 reference signature 和表达去卷积假设，适合生成群体层面证据，但不能替代单细胞验证。

PathSeq、lefser、Kraken2 和 Stereo-seq SAW 用于微生物 reads 识别和空间定位。微生物 reads 在人组织转录组中常有低丰度和污染风险，因此本文结合 saliva、FISH、Gram stain、IHC 和 spatial transcriptomics 增强可信度。

#### 验证策略、稳健性和混杂控制

driver genes 通过独立 48 个 IM 样本、正常胃研究、TCGA pan-GI cancer 和 IntOGen 胃癌 driver lists 做外部/内部交叉验证。KRAS/MAPK RNA-seq 结果通过 1,000 次 down-sampling 控制组间样本数不平衡。CH 风险结果通过排除测序深度偏离均值 ±1 SD 的样本进行敏感性分析，说明 coverage 差异不是主要驱动。

微生物和免疫结果用 scRNA-seq、bulk deconvolution、saliva metagenomics、FISH、IHC、Stereo-seq 多种证据链互相支持。弱点是空间和单细胞样本量较小，且许多分析是横断面关联。

#### 可重复性资源和迁移注意点

原始数据存放在 EGA：EM-seq、WGS、targeted sequencing、transcriptomic sequencing 以及 GCEP1000 相关 targeted panel、bulk RNA-seq、WGS、scRNA-seq 均需向 Singapore Gastric Cancer Consortium Data Access Committee 申请。

迁移到自己的 IM 队列时，最关键的是测序深度和 paired germline。低 VAF IM 突变不能用常规低深度 WES 直接复现；CH 分析也需要可靠 blood/saliva germline sequencing，并要处理白细胞污染、panel of normals 和 CH VAF 阈值。若做微生物分析，需要独立的污染控制、阴性对照和原位验证。

#### 关键复现参数

- Targeted panel：Agilent SureSelect XT HS2 custom tier 2；每个样本 100 ng DNA，16 个样本等量合并至每次 hybridisation 1.5 μg；NovaSeq 6000 PE150。Reads 对齐 hs37d5，并用 molecular barcode 去重复。深测序 Mutect2 使用 `--force-active true --pruning-lod-threshold -4 --max-reads-per-alignment-start 0`，再经过 gnomAD、panel of normals、contamination 和 orientation-artifact filters；最终至少 5 条 variant-supporting reads 且 VAF ≥1%（`P018.S0009–P018.S0031`）。
- WGS：NEBNext Ultra II DNA Library Prep Kit 建库，NovaSeq 6000 PE150，20 对 IM–normal 样本平均覆盖 60.5×；对齐 hs37d5 后以 MarkDuplicates 处理重复 reads（`P003.S0022`、`P018.S0017–P018.S0026`）。
- Hp/CagA：六个 Hp genes 覆盖 ≥1× 才进入系统发育；961 个 SNVs，RAxML `GTRGAMMA`，FDR <0.05；AlphaFold 3 输入 CagA aa 1–251 与 ASPP2 aa 684–891，原子距离 ≤3.5 Å 定义接触。HEK293T 转染 48 小时后裂解，IP 抗体/磁珠在 4°C overnight，4%–20% SDS-PAGE；co-IP 结果为四次独立重复（`P018.S0032–P019.S0012`）。
- Organoid 培养液：50% Wnt3A-conditioned、10% R-Spondin-1-conditioned、HEPES 10 mmol/L、GlutaMAX 2 mmol/L、B27 1×、N-acetyl-L-cysteine 1 mmol/L、EGF 50 ng/mL、FGF10 100 ng/mL、noggin 100 ng/mL、gastrin I 1 nmol/L、A83-01 2 μmol/L、Y-27632 10 μmol/L。活力实验每孔 1,000 cells/5 μL Matrigel，处理 3 天；colony assay 每孔 500 cells/5 μL，pyrvinium 100 nmol/L；IC50 用 GraphPad Prism 10.2.3，IM/normal 比较用 `lme4`/`lmerTest`，colony 多重比较用 two-stage Benjamini–Krieger–Yekutieli、Q=1%（`P019.S0022–P019.S0041`）。
- OXPHOS/氧化损伤：Seahorse 每孔约 150 个、平均直径约 100 μm 的 organoids，依次加入 oligomycin A 5 μmol/L、FCCP 0.5 μmol/L、rotenone 2 μmol/L 与 antimycin A 2 μmol/L；DCA 5 mmol/L 预处理 24 小时，OCR 按 DNA 量归一。ROS 用 CellROX 10 μmol/L、37°C 30 分钟；γH2AX 在 4°C 染色 30 分钟（`P020.S0015–P020.S0035`）。
- EM-seq：200 ng genomic DNA 加 lambda negative 与 methylated pUC19 positive controls，Covaris 打断至平均 300 bp，NovaSeq X Plus PE150；BWA-Meth、Picard MarkDuplicates、MethylDackel。Controls 平均甲基化为 1.5% 与 97.5%；methylKit 阈值 FDR <0.001、差异 >10%，聚类用 top 50% variable CpG、Pearson distance、Ward.D2（`P020.S0036–P020.S0045`）。
- CH/临床模型：blood/saliva 作为 Mutect2 “tumor”、matched IM 作为 control，并关闭 normal-artifact filter；至少 5 条支持 reads、blood/saliva VAF ≥2%，且至少为 matched IM VAF 的 2×。Logistic regression 用 R `glm`；GCEP1000 取最早胃窦 biopsy，排除既往 HGD/胃癌和 OLGIM I，近期国际样本只用 baseline outcome，最终 765 人（43 dysplasia、26 EGN）（`P020.S0046–P021.S0014`）。
- Saliva/microbiome：采集 2 mL 唾液，50°C 60 分钟后每份 500 μL、−80°C 保存；250 μL 用 PowerFecal Pro 提取，6.0 m/s bead-beating 40 秒；NovaSeq X Plus PE150、约 6 GB/样本。PathSeq abundance 以 bacterial/human reads ×10^6 归一；bacterial reads <0.02% 的 RNA-seq 样本排除；lefser 比较菌属，CIBERSORTx relative mode 推断 7 类免疫细胞，ESTIMATE 计算 immune score（`P021.S0015–P021.S0035`）。
- 原位验证：IHC 的 MPO/CXCL8/CXCL2 分别为 1:10,000、1:100、1:50；Gram stain 为 crystal violet 与 safranin 各 1 分钟。FISH probe 1 μmol/L，88°C 3 分钟预热、42°C overnight；Stereo-seq 用 5 μm FFPE、SAW `--detect-microorganism` 与 Kraken2，在 bin50 中去除 bacterial counts <5，并过滤 genes <3、total counts <20 或 mitochondrial transcripts >5% 的 bins（`P021.S0036–P022.S0028`）。

### Methods 证据覆盖审计

| 原文句子 ID | 忠实中文含义 | 方法学解释 | 复现注意点 |
|---|---|---|---|
| `P018.S0004–P018.S0008`（5/5） | 六地伦理审批、书面知情同意和 Helsinki 声明。 | 界定多中心人体样本合规性。 | 逐中心纳排标准主要在缺失 Supplementary Table S1。 |
| `P018.S0009–P018.S0031`（23/23） | Targeted/WGS 建库、PE150、hs37d5、去重复、HaplotypeCaller/Mutect2 与最终过滤。 | 高深度 panel 以灵敏度换取基因组广度。 | Mutect2 为提高灵敏度修改参数；1% VAF 和 5-read 阈值依赖深度。 |
| `P018.S0032–P019.S0014`（31/31） | Hp coverage/phylogeny、CagA–ASPP2 结构和 co-IP，以及 bulk/scRNA 数据构成。 | 把地区菌株变异连接到蛋白互作，并说明转录组复用。 | “two-way” t test 原文措辞低置信；bulk 104、scRNA 18，其中新增 high-CH 为 10/2。 |
| `P019.S0015–P019.S0021`（7/7） | IntOGen 七算法与 weighted voting、artifact removal；fgsea 的 KRAS/ERK/intersection top 200。 | Driver discovery 与转录通路验证。 | 候选受 277-gene panel 限制；scRNA cell-cycle 句跨栏截断，细节依赖既往方法。 |
| `P019.S0022–P020.S0007`（34/34） | Organoid 培养、RNA-seq、batch correction、药物/colony assay、western blot 与 CDX2/EPCAM staining。 | 在正常与 IM 来源类器官中验证状态和药物敏感性。 | Supplementary Fig. S1D 的逐剂量矩阵不在本地 PDF；遗传扰动缺失。 |
| `P020.S0008–P020.S0045`（38/38） | SigProfiler、8-oxo-dG、Seahorse/DCA、ROS/γH2AX、EM-seq、QC 和 methylKit。 | 连接 signature、代谢/氧化读出与甲基化区域。 | 这些实验没有纵向积累 SBS17 的读出，不能闭合机制。 |
| `P020.S0046–P021.S0014`（18/18） | 反向 CH calling、MSKCC 对照、临床 endpoint、`glm`、纳排和 765 人构成。 | 区分血液克隆与 IM/白细胞污染，并建立临床关联模型。 | Results/Methods 的 MSKCC 总人数不一致；26 个 EGN 限制模型稳定性。 |
| `P021.S0015–P022.S0028`（70/70） | 唾液 shotgun、PathSeq/lefser、CIBERSORTx/ESTIMATE、IHC、Gram、FISH、Stereo-seq/SAW/Kraken2 与 QC。 | 用多模态证据连接菌属、免疫组成与空间炎症。 | Panel/转录组并非专为低丰度微生物设计；FISH/Stereo-seq 来自胃癌，样本少。 |

审计结论：主 Methods 连续范围 `P018.S0004–P022.S0028` 的 226/226 个 ID 已覆盖，未覆盖 ID：无；数据可用性 `P022.S0029–P022.S0033` 的 5/5 个 ID 已覆盖。Manifest 自动标为 `methods` 的 115 个 ID 均属主 Methods；后 111 个真实 Methods ID 被误标为 `supplementary`，已全部人工校正。

### 生物学与临床意义

这篇文章把 IM 风险从“病理分期 + Hp 暴露”推进到“上皮克隆演化 + 突变过程 + 系统性造血克隆 + 黏膜免疫微生物生态”。ARID1A truncation、SBS17 和 high CH 是值得进入独立纵向验证的候选分子变量，但目前还不能用于识别单个患者的真实进展概率。

临床转化边界也很清楚：这些 marker 目前不能替代内镜和病理，也不能直接指导药物干预。更现实的近期工作是把分子指标预先写入外部验证方案，检验其能否在 OLGIM、年龄和性别之外稳定改善校准、决策曲线和随访资源分配。

### 局限性与危险假设

第一，国际样本随访时间短，很多国家的临床结局是 baseline observation，因此“进展风险”仍主要依赖少量事件和新加坡长期队列。第二，靶向 panel 无法发现 panel 外 driver、结构变异和非编码调控突变。第三，SBS17 与 OXPHOS 的机制关系仍是相关性，缺少长期扰动后突变累积读出。第四，pyrvinium 的类器官结果提示可干预性，但药物选择性、毒性、体内可达性和真实预防效果都未证明。第五，微生物结果存在低丰度 reads、污染和因果方向问题，尽管作者用了多模态证据降低风险。

### 证据强度、原文冲突与不能外推的结论

**直接数据支持：** 高深度 panel 能比约 60× WGS 或模拟 100× WES 检出更多低 VAF IM mutations；ARID1A truncation、high CH 与 EGN 在本队列内相关；KRAS/MAPK-altered IM 有相应转录程序；SBS17 与 late replication、吸烟和低甲基化区域相关；high CH 组的免疫/微生物组成存在横断面差异。

**合理但尚未直接证明：** OXPHOS 造成 SBS17；CH 先促成 PIGR truncation，再破坏 IgA 屏障、允许口腔菌扩增并推动 IM 进展；pyrvinium 能安全阻断人体癌前演化；加入这些分子变量后会改善真实临床净获益。

**原文数字和解析冲突：**

- MSKCC 对照总人数在 Results `P012.S0020`/Fig. 5 图注为 24,146，在 Methods `P021.S0003` 为 24,126；不能静默统一。
- Fig. 5A 以 1,067 名 subjects 为分母；Fig. 5C 图注却写 234 CHIP-positive 加 861 CHIP-negative IM samples，共 1,095 份。受试者与样本可能重复，主 PDF 未给逐一映射。
- `P019.S0010–P019.S0012` 把 CagA co-IP 的检验写成 “Student t test (two-way)”。这可能意指 two-tailed，但原文没有澄清，本笔记保留原措辞。
- Fig. 3–6 跨双栏/跨页，`P007.S0043–P009.S0002`、`P011.S0042–P012.S0005` 和 `P012.S0052–P015.S0002` 被抽取器拆开；图页坐标轴文字不能单独当作结果来源。
- 数据可用性在 `P022.S0033` 跨栏后截断于 “Data”；八个 accession 可完整读出，但申请机构名称需结合正文语境理解。

**不能从本研究外推：** 不能把横断面关联写成 CH 导致胃黏膜改变；不能把胃癌组织中的 Streptococcus 空间重叠当作 IM 原位验证；不能把 AUC 提升当作已经外部验证或校准的随访工具；不能把类器官活力下降写成人体预防疗效；也不能认为 277-gene panel 已覆盖全部 IM driver 和突变过程。

### 深度研究洞察

最值得学习的是作者把 CH 引入胃癌癌前病变研究。CH 通常被看作血液系统老化现象，本文则把它作为潜在的系统性修饰因素，连接到 IM epithelial mutations、PIGR、IgA、口腔菌和 EGN 风险。现有数据支持相关网络，不足以证明 CH 是这些黏膜改变的来源。

第二个洞察是 SBS17 的定位。作者没有只说“IM 有 SBS17”，而是把它放在 WGS vs normal/gastric cancer、VAF、replication timing、OXPHOS、8-oxo-dG、吸烟和地理风险中解释。这个多层证据结构比单纯 signature detection 更有说服力。

第三个洞察是高深度 targeted panel 的价值。对于癌前病变，低 VAF 是常态；如果研究问题是早期克隆演化，panel 深度可能比全外显子/全基因组广度更关键。本文为 IM、Barrett、炎症性肠病癌前病变等研究提供了技术论证。

### 可借鉴或迁移的思路

可迁移到胃癌精准预防队列的框架是：OLGIM/病理分层 + high-depth epithelial mutation panel + blood CH panel + smoking/Hp history + oral/gastric microbiome + longitudinal EGN endpoint。若样本量允许，可以把 ARID1A truncation、SBS17 exposure、mutation burden、high CH 和 PIGR status 纳入 joint risk model。

可迁移到机制研究的方向是 CH-high IM 的免疫微环境。可以建立 CH mutation carrier 与 non-carrier 的前瞻 IM biopsy 队列，配套单细胞、空间转录组、IgA repertoire、mucosal microbiome 和外周血炎症因子，验证 TET2/DNMT3A/ASXL1 不同 CH driver 是否对应不同黏膜炎症程序。

可迁移到干预研究的方向包括两类：一类是 KRAS/MEK/ERK/OXPHOS 相关上皮干预，另一类是非 Hp 口腔菌和黏膜免疫屏障干预。前者更接近药物安全性和癌前干预问题，后者更接近 antimicrobial/probiotic/oral hygiene 与胃癌风险的目标试验模拟。

### 可复用学术表达

- “IM is not only a histologic intermediate but an evolutionary state shaped by epithelial and nonepithelial somatic alterations.” 这类表达适合把癌前病变从静态病理概念转为动态演化概念。
- “High-depth targeted sequencing is required when the biological signal resides in low-VAF premalignant clones.” 适合写测序策略理由。
- “CH may act as a systemic modifier of tissue-specific cancer risk through inflammatory and mucosal immune pathways.” 适合写 CH 与实体癌前病变连接的假说。
- “Molecular risk stratification should be interpreted as an addition to, rather than a replacement for, established histopathologic staging.” 适合写临床转化边界。

### 相关论文与概念

- Correa cascade：normal mucosa -> chronic gastritis/atrophy -> IM -> dysplasia -> gastric cancer，是本文所有结果的临床病理坐标。
- OLGIM staging：当前 IM 风险分层基础，适合作为分子模型的临床 backbone。
- SBS17 in upper GI premalignancy：Barrett esophagus、esophageal adenocarcinoma 和胃癌中均有相关观察，可作为跨上消化道癌前病变比较方向。
- Clonal hematopoiesis and solid cancer risk：CH 与肺癌、肝癌、结直肠癌等实体瘤风险的关联为本文提供外部背景。
- PIGR/IgA mucosal barrier：连接上皮突变、免疫屏障和微生物定植的核心生物学概念。
- Streptococcus anginosus in gastric cancer：本文把近期口腔菌-胃癌进展线索推进到原位和空间层面。
