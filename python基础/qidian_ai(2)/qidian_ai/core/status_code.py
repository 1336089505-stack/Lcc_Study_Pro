from enum import Enum


class StatusCodes(Enum):
    """
    状态码
    """
    # 成功
    SUCCESS = (0, "成功")

    # 参数错误 1000
    PARAM_MISSING = (1000, "参数不能为空")
    PARAM_INVALID = (1001, "参数格式不合法")
    PARAM_TYPE_ERROR = (1002, "参数类型错误")

    # 认证 / 登录 2000
    AUTH_FAILED = (2000, "认证失败")
    USERNAME_OR_PASSWORD_ERROR = (2001, "用户名或密码错误")
    TOKEN_EXPIRED = (2002, "登录已过期")
    TOKEN_INVALID = (2003, "无效的登录凭证")
    NO_PERMISSION = (2004, "无权限访问")

    # 业务数据 3000
    DATA_NOT_FOUND = (3000, "数据不存在")
    DATA_ALREADY_EXISTS = (3001, "数据已存在")
    DATA_CONFLICT = (3002, "数据冲突")
    OPERATION_NOT_ALLOWED = (3003, "操作不允许")

    # 系统错误 5000
    SYSTEM_ERROR = (5000, "系统内部错误")
    DATABASE_ERROR = (5001, "数据库错误")

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
