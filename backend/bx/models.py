from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import pre_save

from backend.utils import *


class BiopsyData(models.Model):

    # Baseline characteristics
    owner           = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    initial         = models.CharField(max_length=120, blank=True)
    hospital        = models.CharField(max_length=120, blank=True)

    orderdate       = models.DateField(null=True, blank=True)
    studyenroll     = models.CharField(max_length=120, blank=True)
    studynum        = models.IntegerField(null=True, blank=True)
    studycode       = models.CharField(max_length=120, blank=True)
    professor       = models.CharField(max_length=120, blank=True)
    resident        = models.CharField(max_length=120, blank=True)
    phone_num       = models.CharField(max_length=120, blank=True)
    ward_num        = models.CharField(max_length=120, blank=True)
    sex             = models.CharField(max_length=120, blank=True)
    age             = models.IntegerField(null=True, blank=True)
    height          = models.FloatField(null=True, blank=True)
    weight          = models.FloatField(null=True, blank=True)
    BMI             = models.FloatField(null=True, blank=True)
    SBP             = models.IntegerField(null=True, blank=True)
    DBP             = models.IntegerField(null=True, blank=True)

    smoking         = models.CharField(max_length=120, blank=True)
    smoking_detail  = models.FloatField(null=True, blank=True)
    alcohol         = models.CharField(max_length=120, blank=True)
    alcohol_detail  = models.FloatField(null=True, blank=True)
    chief_complaint = models.CharField(max_length=120, blank=True)
    CC_onset        = models.IntegerField(null=True, blank=True)
    graft_biopsy    = models.CharField(max_length=120, blank=True)
    present_illness = models.TextField(null=True, blank=True)
    clinical_diagnosis = models.CharField(max_length=120, blank=True)

    # Past history
    DM              = models.CharField(max_length=120, blank=True)
    DM_detail       = models.FloatField(null=True, blank=True)
    HTN             = models.CharField(max_length=120, blank=True)
    HTN_detail      = models.FloatField(null=True, blank=True)
    CAD             = models.CharField(max_length=120, blank=True)
    CVA             = models.CharField(max_length=120, blank=True)
    liverdz         = models.CharField(max_length=120, blank=True)
    lungdz          = models.CharField(max_length=120, blank=True)
    cancer          = models.CharField(max_length=120, blank=True)
    HIV             = models.CharField(max_length=120, blank=True)
    familyhx        = models.CharField(max_length=120, blank=True)
    herb            = models.CharField(max_length=120, blank=True)
    NSAID           = models.CharField(max_length=120, blank=True)
    ACEARB          = models.CharField(max_length=120, blank=True)
    medicinehx      = models.CharField(max_length=120, blank=True)
    otherhx         = models.CharField(max_length=120, blank=True)

    # CBC
    WBC         = models.FloatField(null=True, blank=True)
    Hb          = models.FloatField(null=True, blank=True)
    Hct         = models.FloatField(null=True, blank=True)
    PLT         = models.FloatField(null=True, blank=True)
    lympho      = models.FloatField(null=True, blank=True)
    mono        = models.FloatField(null=True, blank=True)
    neutro      = models.FloatField(null=True, blank=True)
    ANC         = models.FloatField(null=True, blank=True)
    eosino      = models.FloatField(null=True, blank=True)
    baso        = models.FloatField(null=True, blank=True)
    PT          = models.FloatField(null=True, blank=True)
    aPTT        = models.FloatField(null=True, blank=True)

    # Chemistry
    T_prot      = models.FloatField(null=True, blank=True)
    Alb         = models.FloatField(null=True, blank=True)
    Gluc        = models.FloatField(null=True, blank=True)
    BUN         = models.FloatField(null=True, blank=True)
    Cr          = models.FloatField(null=True, blank=True)
    T_bil       = models.FloatField(null=True, blank=True)
    AST         = models.FloatField(null=True, blank=True)
    ALT         = models.FloatField(null=True, blank=True)
    ALP         = models.FloatField(null=True, blank=True)
    LDH         = models.FloatField(null=True, blank=True)
    UA          = models.FloatField(null=True, blank=True)
    TG          = models.FloatField(null=True, blank=True)
    T_chol      = models.FloatField(null=True, blank=True)
    HDL         = models.FloatField(null=True, blank=True)
    LDL         = models.FloatField(null=True, blank=True)
    Na          = models.FloatField(null=True, blank=True)
    Kal         = models.FloatField(null=True, blank=True)
    Cl          = models.FloatField(null=True, blank=True)
    TCO2        = models.FloatField(null=True, blank=True)
    Ca          = models.FloatField(null=True, blank=True)
    phos        = models.FloatField(null=True, blank=True)
    CRP         = models.FloatField(null=True, blank=True)
    HbA1c       = models.FloatField(null=True, blank=True)
    b2MG        = models.FloatField(null=True, blank=True)
    freeT4      = models.FloatField(null=True, blank=True)
    TSH         = models.FloatField(null=True, blank=True)
    iPTH        = models.FloatField(null=True, blank=True)
    VitD        = models.FloatField(null=True, blank=True) 
    cystatinC   = models.FloatField(null=True, blank=True)
    ionizedCa   = models.FloatField(null=True, blank=True)
    magnesium   = models.FloatField(null=True, blank=True)
    osmolality  = models.FloatField(null=True, blank=True)
    CK          = models.FloatField(null=True, blank=True)
    CKMB        = models.FloatField(null=True, blank=True)
    troponinT   = models.FloatField(null=True, blank=True)
    proBNP      = models.FloatField(null=True, blank=True)
    ferritin    = models.FloatField(null=True, blank=True)
    iron        = models.FloatField(null=True, blank=True)
    TIBC        = models.FloatField(null=True, blank=True)
    TSAT        = models.FloatField(null=True, blank=True)
    folate      = models.FloatField(null=True, blank=True)
    VitB12      = models.FloatField(null=True, blank=True)
    IgG4        = models.FloatField(null=True, blank=True)


    Uprot           = models.CharField(max_length=120, blank=True)
    UWBC            = models.CharField(max_length=120, blank=True)
    URBC            = models.CharField(max_length=120, blank=True)
    dysmorphic      = models.CharField(max_length=120, blank=True)
    Ucast           = models.CharField(max_length=120, blank=True)

    HBsAg           = models.CharField(max_length=120, blank=True)
    anti_HBs        = models.CharField(max_length=120, blank=True)
    anti_HCV        = models.CharField(max_length=120, blank=True)
    anti_HIV        = models.CharField(max_length=120, blank=True)
    RPR             = models.FloatField(null=True, blank=True)

    UV              = models.IntegerField(null=True, blank=True)
    prot24          = models.FloatField(null=True, blank=True)
    Cr24            = models.FloatField(null=True, blank=True)
    Na24            = models.FloatField(null=True, blank=True)
    Kal24           = models.FloatField(null=True, blank=True)
    phos24          = models.FloatField(null=True, blank=True)
    Ca24            = models.FloatField(null=True, blank=True)
    ProtSpot        = models.FloatField(null=True, blank=True)
    CrSpot          = models.FloatField(null=True, blank=True)
    TP_Cr           = models.FloatField(null=True, blank=True)

    C3              = models.FloatField(null=True, blank=True)
    C4              = models.FloatField(null=True, blank=True)
    CH50            = models.FloatField(null=True, blank=True)
    IgM             = models.FloatField(null=True, blank=True)
    IgA             = models.FloatField(null=True, blank=True)
    IgG             = models.FloatField(null=True, blank=True)
    ANA             = models.CharField(max_length=120, blank=True)
    ANAtiter        = models.CharField(max_length=120, blank=True)
    ANA_detail      = models.CharField(max_length=120, blank=True)
    anti_dsDNA      = models.CharField(max_length=120, blank=True)
    ANCA_PR3        = models.CharField(max_length=120, blank=True)
    ANCA_MPO        = models.CharField(max_length=120, blank=True)
    anti_GBM        = models.CharField(max_length=120, blank=True)
    ASO             = models.FloatField(null=True, blank=True)
    RF              = models.FloatField(null=True, blank=True)
    cryoglobulin    = models.CharField(max_length=120, blank=True)

    confirmlab     = models.BooleanField(default=False)

    # Pathologic report
    diagnosis       = models.CharField(max_length=120, blank=True)
    diagnosis_detail= models.CharField(max_length=120, blank=True)
    diag_acc1       = models.CharField(max_length=120, blank=True)
    diag_acc2       = models.CharField(max_length=120, blank=True)
    diagnosis_description = models.TextField(null=True, blank=True)

    total_glom      = models.IntegerField(null=True, blank=True)
    glob_sclerosis  = models.IntegerField(null=True, blank=True)
    seg_sclerosis   = models.IntegerField(null=True, blank=True)
    crescent        = models.IntegerField(null=True, blank=True)
    tuft_adhesion   = models.IntegerField(null=True, blank=True)
    mes_prol        = models.CharField(max_length=120, blank=True)
    mes_expansion   = models.CharField(max_length=120, blank=True)
    endocap_prol    = models.CharField(max_length=120, blank=True)
    glom_description= models.TextField(null=True, blank=True)

    tubule_atrophy  = models.CharField(max_length=120, blank=True)
    tubule_atrophy_perc = models.CharField(max_length=120, blank=True)
    tubule_inflam   = models.CharField(max_length=120, blank=True)
    tubule_inflam_detail = models.CharField(max_length=120, blank=True)
    inter_edema     = models.CharField(max_length=120, blank=True)
    inter_fibrosis  = models.CharField(max_length=120, blank=True)
    inter_fibrosis_perc = models.CharField(max_length=120, blank=True)
    inter_inflam    = models.CharField(max_length=120, blank=True)
    inter_inflam_detail = models.CharField(max_length=120, blank=True)
    ti_description  = models.TextField( null=True, blank=True)
    int_thicken     = models.CharField(max_length=120, blank=True)
    hyalinosis      = models.CharField(max_length=120, blank=True)
    med_sclerosis      = models.CharField(max_length=120, blank=True)
    vessel_description = models.TextField(null=True, blank=True)

    IF_IgG          = models.CharField(max_length=120, blank=True)
    IF_IgA          = models.CharField(max_length=120, blank=True)
    IF_IgM          = models.CharField(max_length=120, blank=True)
    IF_C3           = models.CharField(max_length=120, blank=True)
    IF_C4           = models.CharField(max_length=120, blank=True)
    IF_C1q          = models.CharField(max_length=120, blank=True)
    IF_kappa        = models.CharField(max_length=120, blank=True)
    IF_lambda       = models.CharField(max_length=120, blank=True)
    IF_mesan        = models.CharField(max_length=120, blank=True)
    IF_capillary    = models.CharField(max_length=120, blank=True)
    IF_description  = models.TextField(null=True, blank=True)

    DD              = models.CharField(max_length=120, blank=True)
    DD_mesan        = models.CharField(max_length=120, blank=True)
    DD_subepi       = models.CharField(max_length=120, blank=True)
    DD_subendo      = models.CharField(max_length=120, blank=True)
    GBM_thickness   = models.CharField(max_length=120, blank=True)
    GBM_thick_nm    = models.FloatField(null=True, blank=True)
    foot_efface     = models.CharField(max_length=120, blank=True)
    foot_detail     = models.CharField(max_length=120, blank=True)
    EM_description  = models.TextField(null=True, blank=True)

    confirmpatho    = models.BooleanField(default=False)

    # data 관리를 위한 항목
    slug            = models.CharField(max_length=120, blank=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    update_date     = models.DateTimeField(auto_now=True)

    complete        = models.BooleanField(default=False)
    patientid       = models.IntegerField(null=True,)
    idhospital      = models.CharField(max_length=120, blank=True)
    patientname     = models.CharField(max_length=10, null=True,)


    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.hospital} - {self.patientname} ({self.patientid})"


def rl_pre_save_reciever(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slug_generator(instance)
    if not instance.initial:
        instance.initial = initial_generator(instance)
    if not instance.idhospital:
        instance.idhospital = idhospital_generator(instance)
    if instance.ProtSpot and instance.CrSpot:
        TP_Cr = round((float(instance.ProtSpot) * 1000 / float(instance.CrSpot)), 2)
        if instance.TP_Cr != TP_Cr:
            instance.TP_Cr = TP_Cr
    if instance.HDL and instance.T_chol and instance.TG:
        LDL = float(instance.T_chol) - float(instance.HDL) - (float(instance.TG) / 5)
        if instance.LDL != LDL:
            instance.LDL = LDL

pre_save.connect(rl_pre_save_reciever, sender=BiopsyData)


class CatInfo(models.Model):
    subcat_num      = models.IntegerField(null=True, blank=True)
    subcat_name     = models.CharField(max_length=120, blank=True)
    category        = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return f"{self.subcat_num}. {self.subcat_name}"
    
    
class VarInfo(models.Model):
    variable        = models.CharField(max_length=120, blank=True)
    subcat          = models.ForeignKey(CatInfo, on_delete=models.CASCADE)
    order           = models.IntegerField(null=True, blank=True)
    var_name        = models.CharField(max_length=120, blank=True)
    choice          = models.CharField(max_length=120, blank=True)
    min_value       = models.IntegerField(null=True, blank=True)
    max_value       = models.IntegerField(null=True, blank=True)
    readonly        = models.BooleanField(default=False)
    required        = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subcat}: {self.variable}"
