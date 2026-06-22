# AGENTS.md - 项目上下文

## 项目概述
qoder-ci-test 是一个用于验证 Qoder AI Code Review 的极简 Flask 测试项目。
技术栈：Python 3.11 / Flask / SQLite

## 项目结构
```
app.py              # 主应用（含若干故意留的代码问题）
requirements.txt    # Python 依赖
```

## 审查重点（按优先级）
1. 安全：所有数据库查询必须使用参数化查询，禁止字符串拼接
2. 安全：API 接口必须进行权限验证，敏感信息不得硬编码
3. 安全：所有外部输入必须验证和清理
4. 安全：密码存储必须使用 bcrypt 或 argon2，禁止 MD5
5. 性能：N+1 查询检测，大数据量操作要分页

## 可以忽略的检查
- 这是一个测试项目，不需要关注部署配置
- 不需要关注日志和监控

## 编码约定
- 异步操作：使用 async/await
- 命名：函数 snake_case，常量 UPPER_SNAKE_CASE
- 错误处理：业务异常用自定义 Exception，不裸抛 Exception
- 提交：遵循 Conventional Commits（feat/fix/refactor/docs/test）
