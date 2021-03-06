# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..regutils import RegAverage


def test_RegAverage_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        avg_files=dict(
            argstr="-avg %s",
            position=1,
            sep=" ",
            xor=[
                "avg_lts_files",
                "avg_ref_file",
                "demean1_ref_file",
                "demean2_ref_file",
                "demean3_ref_file",
                "warp_files",
            ],
        ),
        avg_lts_files=dict(
            argstr="-avg_lts %s",
            position=1,
            sep=" ",
            xor=[
                "avg_files",
                "avg_ref_file",
                "demean1_ref_file",
                "demean2_ref_file",
                "demean3_ref_file",
                "warp_files",
            ],
        ),
        avg_ref_file=dict(
            argstr="-avg_tran %s",
            extensions=None,
            position=1,
            requires=["warp_files"],
            xor=[
                "avg_files",
                "avg_lts_files",
                "demean1_ref_file",
                "demean2_ref_file",
                "demean3_ref_file",
            ],
        ),
        demean1_ref_file=dict(
            argstr="-demean1 %s",
            extensions=None,
            position=1,
            requires=["warp_files"],
            xor=[
                "avg_files",
                "avg_lts_files",
                "avg_ref_file",
                "demean2_ref_file",
                "demean3_ref_file",
            ],
        ),
        demean2_ref_file=dict(
            argstr="-demean2 %s",
            extensions=None,
            position=1,
            requires=["warp_files"],
            xor=[
                "avg_files",
                "avg_lts_files",
                "avg_ref_file",
                "demean1_ref_file",
                "demean3_ref_file",
            ],
        ),
        demean3_ref_file=dict(
            argstr="-demean3 %s",
            extensions=None,
            position=1,
            requires=["warp_files"],
            xor=[
                "avg_files",
                "avg_lts_files",
                "avg_ref_file",
                "demean1_ref_file",
                "demean2_ref_file",
            ],
        ),
        environ=dict(nohash=True, usedefault=True,),
        omp_core_val=dict(argstr="-omp %i", usedefault=True,),
        out_file=dict(argstr="%s", extensions=None, genfile=True, position=0,),
        warp_files=dict(
            argstr="%s", position=-1, sep=" ", xor=["avg_files", "avg_lts_files"],
        ),
    )
    inputs = RegAverage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_RegAverage_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = RegAverage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
