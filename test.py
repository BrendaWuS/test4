# from github import Github
# import os
#
# # 所有权限令牌token
# token = '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'
# # 创建Github对象
# g = Github(token)
#
# # 获取要操作的仓库
# owner = 'BrendaWuS'
# repo = 'test4'
# repository = g.get_repo(f"{owner}/{repo}")
#
# # 项目目录路的根路径
# root_directory = os.path.dirname(os.path.abspath(__file__))
#
#
# # 添加文件、提交更改和推送到远程仓库的函数
# def add_directory(directory_path):
#     for root, dirs, files in os.walk(directory_path):
#         for file in files:
#             file_path = os.path.join(root, file)
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 content = f.read()
#                 # 计算文件相对于项目根路径的相对路径
#                 relative_path = os.path.relpath(file_path, directory_path)
#
#                 try:
#                     # 尝试创建文件
#                     repository.create_file(relative_path, "Add file", content)
#                 except Exception:
#                     # 文件已存在，尝试更新文件
#                     file = repository.get_contents(relative_path)
#                     repository.update_file(file.path, "Update file", content, file.sha)
#
#
# def commit_changes():
#     # 递归地添加项目目录下的所有文件
#     add_directory(root_directory)
#
#     # 获取默认分支的引用
#     ref = repository.get_git_ref(f"heads/{repository.default_branch}")
#
#     # 获取最新提交
#     latest_commit = repository.get_commit(ref.object.sha)
#
#     # 创建新的提交
#     repository.create_git_commit("Commit message", latest_commit.commit.tree, [latest_commit])
#
#
# def push_changes():
#     # 强制更新引用，以便推送更改
#     ref = repository.get_git_ref(f"heads/{repository.default_branch}")
#     ref.edit(ref.object.sha, force=True)
#
#
# # 调用相关函数进行操作
# commit_changes()
# push_changes()

#########上述代码时好时坏############

from github import Github
import os

# 所有权限令牌token
token = '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'
# 创建Github对象
g = Github(token)

# 获取要操作的仓库
owner = 'BrendaWuS'
repo = 'test4'
repository = g.get_repo(f"{owner}/{repo}")

# 项目目录路的根路径
root_directory = os.path.dirname(os.path.abspath(__file__))


# 添加文件、提交更改和推送到远程仓库的函数
def add_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # 计算文件相对于项目根路径的相对路径
                relative_path = os.path.relpath(file_path, directory_path)

                try:
                    # 尝试获取文件对象
                    file_obj = repository.get_contents(relative_path)

                    # 比较文件内容是否相同
                    if file_obj.content != content:
                        # 文件内容发生变化，进行更新
                        repository.update_file(file_obj.path, "Update file", content, file_obj.sha)
                except Exception:
                    # 文件不存在，进行创建
                    repository.create_file(relative_path, "Add file", content, branch=repository.default_branch)


def commit_changes():
    # 递归地添加项目目录下的所有文件
    add_directory(root_directory)

    # 获取默认分支的引用
    ref = repository.get_git_ref(f"heads/{repository.default_branch}")

    # 获取最新提交
    latest_commit = repository.get_commit(ref.object.sha)

    # 获取最新提交的树对象
    latest_tree = latest_commit.commit.tree

    # 创建新的提交
    new_commit = repository.create_git_commit("Commit message", latest_tree, [latest_commit])

    # 更新引用
    ref.edit(new_commit.sha, force=True)


# 调用相关函数进行操作
commit_changes()
