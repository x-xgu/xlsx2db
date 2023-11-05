def abs_path_from_project(relative_path: str):
    """
    获取文件的绝对路径

    需要导入根目录：import core
    relative_path 从项目目录开始：core/utilities/project.py
    """

    import core
    from pathlib import Path
    return Path(
        core.__file__
    ).parent.parent.joinpath(relative_path).absolute().__str__()
