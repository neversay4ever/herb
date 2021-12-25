from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Species(models.Model):
    """ 样本的物种信息 """
    herb_id = models.SmallIntegerField(_("药物编码"))
    herb_name = models.CharField(_("药物名称"), max_length=250)
    herb_pinyin = models.CharField(_("药物拼音"), max_length=250)
    seq_or_not = models.CharField(_("是否测序"), max_length=10)
    daodi_or_not = models.CharField(_("是否道地药材"), max_length=10)
    plant_name = models.CharField(_("植物名称"), max_length=250)
    palnt_class = models.CharField(_("分类纲"), max_length=250)
    plant_order = models.CharField(_("分类目"), max_length=250)
    plant_family = models.CharField(_("分类科"), max_length=250)
    plant_genus = models.CharField(_("分类属"), max_length=250)
    plant_species = models.CharField(_("分类种"), max_length=250)
    species_suffix = models.CharField(_("种后缀"), max_length=250)
    tissue = models.CharField(_("用药组织"), max_length=250)
    origin = models.CharField(_("地源"), max_length=250)
    herb_pic = models.CharField(_("药物图片名称"), max_length=150)
    plant_pic = models.CharField(_("植物图片名称"), max_length=150)
    taste = models.CharField(_("药-味"), max_length=250)
    nature = models.CharField(_("药-性"), max_length=250)
    toxin = models.CharField(_("药-毒"), max_length=250)
    guijing = models.CharField(_("药-归经"), max_length=250)
    gongneng = models.CharField(_("药-功能"), max_length=250)

    def __str__(self):
        return self.herb_name


class Sample(models.Model):
    """ 采样信息，原始测序数据信息 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    herb_name = models.CharField(_("药物名称"), max_length=250)
    herb_name_note = models.CharField(_("药物名称注释"), max_length=250)
    tissue_id = models.CharField(_("组织编号"), max_length=250)
    seq_id = models.CharField(_("测序编号"), max_length=250)
    collection_tissue = models.CharField(_("采样组织"), max_length=250)
    collection_tissue_detail = models.CharField(_("采样组织细节"), max_length=250)
    collection_location = models.CharField(_("采样地点"), max_length=250)
    collection_datetime = models.CharField(_("采样时间"), max_length=150)
    collector = models.CharField(_("采样人"), max_length=250)
    lattitude = models.CharField(_("纬度"), max_length=50)
    longitude = models.CharField(_("经度"), max_length=50)
    elevation = models.CharField(_("海拔"), max_length=50)
    sample_pic_name = models.CharField(_("样本照片名称"), max_length=250)
    field_store_condition = models.CharField(_("野外保存条件"), max_length=250)
    field_store_duration = models.CharField(_("野外保存时间"), max_length=250)
    temporary_store_condition = models.CharField(_("临时保存条件"), max_length=250)
    transport_datetime = models.CharField(_("运输日期"), max_length=150)
    transport_store_condition = models.CharField(_("运输保存条件"), max_length=250)
    receiver = models.CharField(_("样本接收人"), max_length=250)
    receive_datetime = models.CharField(_("样本接收时间"), max_length=150)
    sample_count = models.CharField(_("样本数量"), max_length=50)
    sample_total_weight = models.CharField(_("样本重量"), max_length=50)
    sample_notes = models.TextField(_("样本说明"))
    sample_batch_notes = models.TextField(_("样本批次说明"))
    sequencing_sample_id = models.CharField(_("测序样本ID"), max_length=250)
    sequencing_length_type = models.CharField(_("测序长度类型"), max_length=250)
    barcode_id = models.CharField(_("条形码ID"), max_length=250)
    chip_id = models.CharField(_("芯片ID"), max_length=250)
    lane_id = models.CharField(_("Lane ID"), max_length=250)
    sequencing_platform = models.CharField(_("测序平台"), max_length=250)
    fq1_path = models.CharField(_("fq1文件路径"), max_length=250)
    fq2_path = models.CharField(_("fq2文件路径"), max_length=250)

    def __str__(self):
        return self.herb_name


class Assembly(models.Model):
    """ 组装和注释结果信息 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    tissue_id = models.CharField(_("样本组织编码"), max_length=250)
    gene_id = models.CharField(_("基因ID"), max_length=250)
    gene_length = models.CharField(_("基因长度"), max_length=250)
    gene_seq = models.TextField(_("基因序列"))


class Cpc(models.Model):
    """ 判断组装序列是否为编码序列 """
    # ID     transcript_length       peptide_length  Fickett_score   pI      ORF_integrity   coding_probability      label
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    transcript_length = models.SmallIntegerField(_("转录本长度"))
    peptide_length = models.SmallIntegerField(_("肽段长度"))
    fickett_score = models.FloatField(_("fickett值"))
    pi = models.FloatField(_("pi值"))
    orf_integrity = models.FloatField(_("orf完整度"))
    coding_probability = models.FloatField(_("编码可能性"))
    label = models.CharField(_("标签"), max_length=250)


class Cog(models.Model):
    """ COG 注释 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    cog_id = models.CharField(_("COG ID"), max_length=250)
    cog_evalue = models.FloatField(_("COG e值"))
    cog_description = models.TextField(_("COG说明"))


class Kegg(models.Model):
    """ KEGG 注释 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    kegg_id = models.CharField(_("KEGG ID"), max_length=250)
    kegg_evalue = models.FloatField(_("KEGG e值"))
    kegg_description = models.TextField(_("KEGG说明"))


class Kog(models.Model):
    """ KOG 注释 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    kog_evalue = models.FloatField(_("KOG e值"))
    kog_id = models.CharField(_("KOG ID"), max_length=250)
    kog_description = models.TextField(_("KOG说明"))


class Nr(models.Model):
    """ NR 注释 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    nr_id = models.CharField(_("NR ID"), max_length=250)
    nr_evalue = models.FloatField(_("NR e值"))
    nr_description = models.TextField(_("NR说明"))


class Pfam(models.Model):
    """ Pfam 注释 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    pfam_id = models.CharField(_("Pfam ID"), max_length=250)
    pfam_evalue = models.FloatField(_("Pfam e值"))
    pfam_description = models.TextField(_("Pfam说明"))


class Swissprot(models.Model):
    """ SwissProt 注释 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    swissprot_evalue = models.FloatField(_("SwissProt e值"))
    swissprot_id = models.CharField(_("SwissProt ID"), max_length=250)
    swissprot_description = models.TextField(_("SwissProt说明"))


class Go(models.Model):
    """ GO 注释 """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    go_id = models.CharField(_("GO ID"), max_length=250)
    go_definition = models.TextField(_("GO描述"))
    go_ontology = models.CharField(_("GO 本体"), max_length=250)
    go_term = models.CharField(_("GO 术语"), max_length=250)


class Ssr(models.Model):
    """ SSR 结果 
    ID	         SSR_nr SSR_type	SSR	size	start	end
    scaffold30_1	6	p2	(TA)6	12	9013	9024
    scaffold12_1	31	p2	(TG)12	24	76920	76943
    scaffold12_1	36	p2	(TG)6	12	81729	81740
    scaffold231_2	602	c	(CA)8ctctcactctctca(CT)12	54	1759093	1759146
    第一列：ID，记录SSR所在的位置，如chromsome号，或者Gene ID 等。
    第二列：SSR nr, 表示每个相同ID的SSR编号，即相同ID所包含的第几个SSR
    第三列：SSR type, 表示SSR类型：
    p1，单碱基重复（Mono repeats），如(A)10
    p2，双碱基重复（Di repeats），如(CA)8
    p3，三碱基重复（Tri repeats），如(ACT)6
    p4，四碱基重复（Quad repeats），如(ATCT)5
    p5，五碱基重复（Penta repeats），如(TCATG)7
    p6，六碱基重复（Hexa repeats）），如(CATAAG)7
    c，复合微卫星（repeats with compound），如(A)10tagt(AT)7
    第四列：SSR，表示该SSR的序列特征
    如示例中，(TA)6， 表示有6个TA重复
    (CA)8ctctcactctctca(CT)12 表示，8个CA的重复，随后有一串ctctcactctctca序列，然后再接12个CT重复
    第五列：size，表示该SSR的大小
    第六列：start，表示该SSR的起始位置
    第七列：end，表示该SSR的的终止位置
    """
    herb_id = models.CharField(_("药物编码"), max_length=250)
    gene = models.CharField(_("基因名称"), max_length=250)
    ssr_nr = models.SmallIntegerField(_("SSR编号"))
    ssr_type = models.CharField(_("SSR类型"), max_length=50)
    ssr_pattern = models.TextField(_("SSR模式"))
    ssr_size = models.SmallIntegerField(_("SSR大小"))
    ssr_start = models.PositiveIntegerField(_("SSR起点"))
    ssr_end = models.PositiveIntegerField(_("SSR终点"))
