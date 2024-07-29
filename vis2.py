import trimesh

# 从ply文件加载三维模型数据
mesh = trimesh.load('colmap_dense/fused.ply')

# 显示三维模型
mesh.show()
