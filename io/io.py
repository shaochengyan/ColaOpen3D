import open3d


def read_point_cloud(filename, format='auto', remove_nan_points=False, remove_infinite_points=False, print_progress=False):
    """ 读取指定格式的点云数据,并指定是否移除NaN/Infinite的值
    filename (str) – Path to file.
    format (str, optional, default='auto') – The format of the input file. When not specified or set as auto, the format is inferred from file extension name.
    remove_nan_points (bool, optional, default=False) – If true, all points that include a NaN are removed from the PointCloud.
    remove_infinite_points (bool, optional, default=False) – If true, all points that include an infinite value are removed from the PointCloud.
    print_progress (bool, optional, default=False) – If set to true a progress bar is visualized in the console
    """
    return open3d.io.read_point_cloud(filename, format, remove_nan_points, remove_infinite_points, print_progress)
