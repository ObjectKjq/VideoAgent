# AI 视频生成器 - 项目文档

## 技术架构

### 前端技术栈

| 技术           | 版本   | 用途        |
| -------------- | ------ | ----------- |
| Vue            | 3.5.31 | 前端框架    |
| TypeScript     | 6.0.0  | 类型系统    |
| Vite           | 8.0.3  | 构建工具    |
| Vue Router     | 5.0.4  | 路由管理    |
| Pinia          | 3.0.4  | 状态管理    |
| Ant Design Vue | 4.2.6  | UI 组件库   |
| Axios          | 1.15.0 | HTTP 客户端 |

## 项目结构

```
video-agent/
├── frontend/                   # 前端项目
    ├── src/
    │   ├── api/                # API 接口
    │   ├── assets/             # 静态资源
    │   ├── components/         # 组件
    │   ├── layout/             # 布局组件
    │   ├── router/             # 路由配置
    │   │   └── index.ts
    │   ├── stores/             # 状态管理
    │   ├── views/              # 页面视图
    │   ├── App.vue             # 根组件
    │   ├── main.ts             # 入口文件
    │   └── request.ts          # Axios 配置
    ├── openapi2ts.config.ts    # OpenAPI 生成配置
    ├── vite.config.ts          # Vite 配置
    └── package.json            # 项目配置
```

## 核心功能模块

### 1. 认证授权系统

#### Session 认证机制

- 基于 Cookie 的 Session 认证
- Session ID 使用 UUID 生成
- Session 存储在内存中
- Session 有效期：30 天

#### 权限控制

- **用户角色**：`user`（普通用户）、`admin`（管理员）
- **权限装饰器**：
  - `require_login`：要求用户已登录
  - `require_admin`：要求用户为管理员

### 2. 异常处理系统

#### 错误码定义

| 错误码 | 说明           |
| ------ | -------------- |
| 0      | 成功           |
| 40000  | 请求参数错误   |
| 40100  | 未登录         |
| 40101  | 无权限         |
| 40103  | 密码错误       |
| 40300  | 禁止访问       |
| 40400  | 请求数据不存在 |
| 40401  | 用户不存在     |
| 40402  | 用户已存在     |
| 50000  | 系统内部异常   |
| 50001  | 操作失败       |

#### 统一响应格式

```json
{
  "code": 0,
  "data": {},
  "message": "操作成功"
}
```

## 架构设计原则

### 前端架构

采用组件化开发：

1. **Views**：页面级组件
2. **Components**：可复用组件
3. **API**：接口封装，类型安全
4. **Stores**：全局状态管理

### 代码规范

- 后端遵循 PEP 8 规范
- 前端使用 TypeScript 强类型
- 使用 Pydantic 进行数据验证
- 统一的异常处理机制
- RESTful API 设计风格

## 常见问题

### 3. API 类型生成

修改后端接口后，需运行 `npm run openapi2ts` 重新生成前端类型定义。
