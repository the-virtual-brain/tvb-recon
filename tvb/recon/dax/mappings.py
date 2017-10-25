from enum import Enum


class Inputs(Enum):
    T1_INPUT = "t1_input.nii.gz"
    DWI_INPUT = "dwi_input.mif"
    FS_LUT = "fs_color_lut.txt"
    FS_DEFAULT = "fs_default.txt"
    T2_INPUT = "t2_input.nii"
    FLAIR_INPUT = "flair_input.nii.gz"
    CT_INPUT = "ct_input.nii.gz"
    SCHEMA_TXT = "schema.txt"


class T1Files(Enum):
    T1_INPUT_CONVERTED = "t1_input.mgz"
    T2_CONVERTED = "t2.nii.gz"
    FLAIR_CONVERTED = "flair.nii.gz"
    T1_MGZ = "T1.mgz"
    APARC_ASEG_MGZ = "aparc+aseg.mgz"
    T1_NII_GZ = "T1.nii.gz"
    APARC_ASEG_NII_GZ = "aparc+aseg.nii.gz"
    NORM_MGZ = "norm.mgz"
    BRAIN_MGZ = "brain.mgz"
    LH_PIAL = "lh.pial"
    RH_PIAL = "rh.pial"
    LH_CENTERED_PIAL = "lh.centered.pial"
    RH_CENTERED_PIAL = "rh.centered.pial"
    LH_APARC_ANNOT = "lh.aparc.annot"
    RH_APARC_ANNOT = "rh.aparc.annot"


class T1JobNames(Enum):
    MRI_CONVERT = "mri_convert"
    RECON_ALL = "recon"
    AUTORECON3_T2 = "autorecon3-t2"
    AUTORECON3_FLAIR = "autorecon3-flair"
    MRIS_CONVERT = "mris_convert"


class DWIFiles(Enum):
    DWI_RAW_MIF = "dwi_raw.mif"
    DWI_MIF = "dwi.mif"
    MASK_MIF = "mask.mif"
    B0_NII_GZ = "b0.nii.gz"
    MASK_NII_GZ = "mask.nii.gz"
    DWI_RE_MIF = "dwi_re.mif"
    DWI_RE_NII_GZ = "dwi_re.nii.gz"


class DWIJobNames(Enum):
    MRCONVERT = "mrconvert"
    DWIPREPROC = "dwipreproc"
    DWI2MASK = "dwi2mask"
    DWIEXTRACT = "dwiextract"


class CoregFiles(Enum):
    D2T_MAT = "d2t.mat"
    T2D_MAT = "t2d.mat"
    B0_IN_T1 = "b0-in-t1.nii.gz"
    B0_IN_T1_MGZ = "b0-in-t1.mgz"
    T1_IN_D = "t1-in-d.nii.gz"
    APARC_AGEG_IN_D = "aparc+aseg-in-d.nii.gz"


class CoregJobNames(Enum):
    FLIRT = "flirt"
    CONVERT_XFM = "convert-xfm"
    FLIRT_REVERSED = "flirt-reversed"
    BBREGISTER = "bbregister"
    MRI_VOL2VOL = "mri_vol2vol"


class TractsGenFiles(Enum):
    FILE_5TT_MIF = "5tt.mif"
    GMWMI_MIF = "gmwmi.mif"
    FILE_5TTVIS_MIF = "5ttvis.mif"
    RESPONSE_TXT = "response.txt"
    WM_FOD_MIF = "wm_fod.mif"
    FILE_TCK = "%s.tck"
    FILE_SIFT_TCK = "%s.tck"
    TDI_ENDS_MIF = "tdi_ends.mif"
    GM_MIF = "gm.mif"
    CSF_MIF = "csf.mif"
    RF_WM = "RF_WM.txt"
    RF_GM = "RF_GM.txt"
    RF_CSF = "RF_CSF.txt"
    RF_VOXELS = "RF_voxels.mif"
    VOLUME_LBL_NII_GZ = "volume_lbl.nii.gz"
    TRACT_COUNTS = "tract_counts.csv"
    TRACT_LENGHTS = "tract_lengths.csv"
    GMWMI_NII_GZ = "gmwmi.nii.gz"
    TDI_ENDS_NII_GZ = "tdi_ends.nii.gz"


class TractsGenJobNames(Enum):
    JOB_5TTGEN = "ttgen"
    JOB_5TT2GMWMI = "tt2gmwmi"
    JOB_5TT2VIS = "tt2vis"
    DWI2RESPONSE = "dwi2response"
    DWI2FOD = "dwi2fod"
    TCKGEN = "tckgen"
    TCKSIFT = "tcksift"
    TCKMAP = "tckmap"
    LABEL_CONVERT = "labelconvert"
    TCK2CONNECTOME = "tck2connectome"
    DWI2RESPONSE_MSMT = "dwi2response-msmt"
    MSDWI2FOD = "msdwi2fod"


class AsegFiles(Enum):
    ASEG_MGZ = "aseg-%06d.mgz"
    ASEG_NOT_SMOOTH = "aseg-%06d-notsmooth"
    ASEG_NOT_SMOOTH_MAIN = "lh.aseg-%06d-notsmooth-main"
    ASEG_LBL_LH = "lh.aseg-%06d"
    ASEG_LBL = "aseg-%06d"
    LH_ASEG = "lh.aseg"
    RH_ASEG = "rh.aseg"
    LH_CENTERED_ASEG = "lh.centered.aseg"
    RH_CENTERED_ASEG = "rh.centered.aseg"
    LH_ASEG_ANNOT = "lh.aseg.annot"
    RH_ASEG_ANNOT = "rh.aseg.annot"
    FS_CUSTOM_TXT = "fs_custom.txt"
    CENTERS_TXT = "centers.txt"
    AREAS_TXT = "areas.txt"
    ORIENTATIONS_TXT = "average_orientations.txt"
    CORTICAL_TXT = "cortical.txt"
    RM_TO_APARC_ASEG_TXT = "rm_to_aparc_aseg.txt"
    RM_CORT_TXT = "region_mapping_cort.txt"
    RM_SUBCORT_TXT = "region_mapping_subcort.txt"
    SURF_CORT_ZIP = "surface_cort.zip"
    SURF_SUBCORT_ZIP = "surface_subcort.zip"


class AsegGenJobNames(Enum):
    MRI_PRETESS = "mri_pretess"
    MRI_TESSELLATE = "mri_tessellate"
    MRIS_EXTRACT = "mris_extract_main_component"
    MRIS_SMOOTH = "mris_smooth"
    ASEG_CONCAT = "aseg_concatenation"
    GEN_MAPPING_DETAILS = "gen_mapping_details"


class OutputConvFiles(Enum):
    APARC_ASEG_COR_NII_GZ = "aparc+aseg-cor.nii.gz"
    CONNECTIVITY_ZIP = "connectivity.zip"


class SEEGCompJobNames(Enum):
    MRI_BINARIZE = "mri_binarize"
    LABEL_CT_WITH_DILATION = "label_ct_with_dilation"
    GEN_SCHEMA_TXT = "gen_schema_txt"
    GEN_SEEG_XYZ = "gen_seeg_xyz"


class SEEGCompFiles(Enum):
    CT_RAS_NII_GZ = "ct-ras.nii.gz"
    CT_IN_T1_NII_GZ = "ct-in-t1.nii.gz"
    CT_TO_T1_MAT = "ct_to_t1.mat"
    BRAIN_RAS_NII_GZ = "brain-ras.nii.gz"
    BRAIN_MASK_NII_GZ = "brain-mask.nii.gz"
    MASKED_CT_NII_GZ = "masked-ct.nii.gz"
    DILATED_CT_NII_GZ = "dilated-ct.nii.gz"
    LABELED_CT_NII_GZ = "labeled-ct.nii.gz"
    SEEG_XYZ = "seeg.xyz"


class HeadModelJobNames(Enum):
    MNE_WATERSHED_BEM = "mne_watershed_bem"
    CONVERT_TO_BRAIN_VISA = "convert_to_brain_visa"
    GEN_HEAD_MODEL = "gen_head_model"
    OM_ASSEMBLE = "om_assemble"
    OM_MINVERSER = "om_minverser"


class HeadModelFiles(Enum):
    BRAIN_SURFACE = "%s_brain_surface"
    INNER_SKULL_SURFACE = "%s_inner_skull_surface"
    OUTER_SKIN_SURFACE = "%s_outer_skin_surface"
    OUTER_SKULL_SURFACE = "%s_outer_skull_surface"
    BRAIN_SURFACE_TRI = "%s_brain_surface.tri"
    INNER_SKULL_SURFACE_TRI = "%s_inner_skull_surface.tri"
    OUTER_SKIN_SURFACE_TRI = "%s_outer_skin_surface.tri"
    OUTER_SKULL_SURFACE_TRI = "%s_outer_skull_surface.tri"
    HEAD_MODEL_GEOM = "head_model.geom"
    HEAD_MODEL_COND = "head_model.cond"
    HEAD_MAT = "head.mat"
    HEAD_INV_MAT = "head_inv.mat"


class SeegGainFiles(Enum):
    CORTICAL_PIAL = "cortical.pial"
    SEEG_GAIN_MAT = "seeg_gain.mat"
    SUBCORTICAL_ASEG = "subcortical.aseg"


class SeegGainJobNames(Enum):
    MERGE_SURFACES = "merge_surfaces"
    COMPUTE_SEEG_GAIN = "compute_seeg_gain"


class ProjectionCompFiles(Enum):
    SENS_POSITIONS = "%s.xyz"
    PROJECTION_MAT = "%s_gain.mat"


class ProjectionCompJobNames(Enum):
    COMPUTE_PROJ_MAT = "compute_projection_matrix"


class ResamplingFiles(Enum):
    LH_PIAL_RESAMP = "lh.pial-%s"
    RH_PIAL_RESAMP = "rh.pial-%s"
    LH_CENTERED_PIAL_RESAMP = "lh.centered.pial-%s"
    RH_CENTERED_PIAL_RESAMP = "rh.centered.pial-%s"
    LH_APARC_ANNOT_RESAMP = "lh.aparc-%s.annot"
    RH_APARC_ANNOT_RESAMP = "rh.aparc-%s.annot"

    LH_ASEG_RESAMP = "lh.aseg-%s"
    RH_ASEG_RESAMP = "rh.aseg-%s"
    LH_ASEG_ANNOT_RESAMP = "lh.aseg-%s.annot"
    RH_ASEG_ANNOT_RESAMP = "rh.aseg-%s.annot"


class ResamplingJobNames(Enum):
    MRI_SURF2SURF = "mri_surf2surf"
    MRIS_DECIMATE = "mris_decimate"
