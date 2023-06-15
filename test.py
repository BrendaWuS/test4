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
root_directory = os.path.dirname(__file__)  # E:\pythonProject\GithubTest3


# 添加文件、提交更改和推送到远程仓库的函数
def add_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                # 计算文件相对于项目根路径的相对路径
                relative_path = os.path.relpath(file_path, directory_path)
                # 在指定路径下创建文件并添加内容
                repository.create_file(relative_path, "Add file", content)


def commit_changes():
    # 获取默认分支的引用
    ref = repository.get_git_ref(f"heads/{repository.default_branch}")

    # 获取最新提交
    latest_commit = repository.get_commit(ref.object.sha)

    # 递归地添加项目目录下的所有文件
    add_directory(root_directory)

    # 创建新的提交
    repository.create_git_commit("Commit message", latest_commit.commit.tree, [latest_commit])


def push_changes():
    # 强制更新引用，以便推送更改
    ref = repository.get_git_ref(f"heads/{repository.default_branch}")
    ref.edit(ref.object.sha, force=True)


# 调用相关函数进行操作
commit_changes()
push_changes()