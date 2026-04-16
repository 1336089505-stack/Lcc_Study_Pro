from db.model import Base
from db.session import engine
from schema.schema_module import BookModel
from service.book_service import BookService

def test_init_db():
    Base.metadata.create_all(engine)

    books = [
        # 1
        BookModel(
            name="Python编程：从入门到实践",
            category="计算机技术",
            binding="平装",
            tags=["畅销书", "新书上架"],
            price=89.9,
            is_sale=True
        ),
        # 2
        BookModel(
            name="Flask Web开发实战",
            category="计算机技术",
            binding="精装",
            tags=["畅销书", "经典名著"],
            price=79.5,
            is_sale=True
        ),
        # 3
        BookModel(
            name="SQLAlchemy权威指南",
            category="计算机技术",
            binding="线装",
            tags=["新书上架", "限时折扣"],
            price=68.8,
            is_sale=False
        ),
        # 4
        BookModel(
            name="数据结构与算法分析",
            category="计算机技术",
            binding="平装",
            tags=["畅销书", "青少年推荐"],
            price=99.0,
            is_sale=True
        ),
        # 5
        BookModel(
            name="深入理解计算机系统",
            category="计算机技术",
            binding="精装",
            tags=["经典名著", "畅销书"],
            price=129.9,
            is_sale=True
        ),
        # 6
        BookModel(
            name="百年孤独",
            category="文学小说",
            binding="精装",
            tags=["经典名著", "畅销书"],
            price=58.0,
            is_sale=True
        ),
        # 7
        BookModel(
            name="三体",
            category="文学小说",
            binding="平装",
            tags=["畅销书", "新书上架", "限时折扣"],
            price=128.5,
            is_sale=True
        ),
        # 8
        BookModel(
            name="白夜行",
            category="文学小说",
            binding="线装",
            tags=["经典名著", "畅销书"],
            price=49.9,
            is_sale=True
        ),
        # 9
        BookModel(
            name="解忧杂货店",
            category="文学小说",
            binding="平装",
            tags=["畅销书", "青少年推荐"],
            price=39.8,
            is_sale=True
        ),
        # 10
        BookModel(
            name="活着",
            category="文学小说",
            binding="精装",
            tags=["经典名著"],
            price=29.9,
            is_sale=False
        ),
        # 11
        BookModel(
            name="明朝那些事儿",
            category="历史传记",
            binding="平装",
            tags=["畅销书", "经典名著"],
            price=168.0,
            is_sale=True
        ),
        # 12
        BookModel(
            name="苏东坡传",
            category="历史传记",
            binding="精装",
            tags=["畅销书", "青少年推荐"],
            price=58.5,
            is_sale=True
        ),
        # 13
        BookModel(
            name="人类简史",
            category="历史传记",
            binding="线装",
            tags=["畅销书", "新书上架"],
            price=68.0,
            is_sale=True
        ),
        # 14
        BookModel(
            name="时间简史",
            category="科普读物",
            binding="平装",
            tags=["畅销书", "经典名著"],
            price=45.8,
            is_sale=True
        ),
        # 15
        BookModel(
            name="果壳中的宇宙",
            category="科普读物",
            binding="精装",
            tags=["新书上架", "限时折扣"],
            price=58.0,
            is_sale=True
        ),
        # 16
        BookModel(
            name="万物简史",
            category="科普读物",
            binding="平装",
            tags=["畅销书", "青少年推荐"],
            price=78.9,
            is_sale=False
        ),
        # 17
        BookModel(
            name="乡土中国",
            category="人文社科",
            binding="线装",
            tags=["经典名著"],
            price=28.0,
            is_sale=True
        ),
        # 18
        BookModel(
            name="乌合之众",
            category="人文社科",
            binding="平装",
            tags=["畅销书", "限时折扣"],
            price=38.5,
            is_sale=True
        ),
        # 19
        BookModel(
            name="理想国",
            category="人文社科",
            binding="精装",
            tags=["经典名著", "青少年推荐"],
            price=45.0,
            is_sale=True
        ),
        # 20
        BookModel(
            name="社会契约论",
            category="人文社科",
            binding="线装",
            tags=["经典名著"],
            price=36.8,
            is_sale=False
        ),
        # 21
        BookModel(
            name="猜猜我有多爱你",
            category="少儿绘本",
            binding="精装",
            tags=["青少年推荐", "新书上架"],
            price=32.9,
            is_sale=True
        ),
        # 22
        BookModel(
            name="DK儿童百科全书",
            category="少儿绘本",
            binding="平装",
            tags=["畅销书", "青少年推荐"],
            price=138.0,
            is_sale=True
        ),
        # 23
        BookModel(
            name="我爸爸我妈妈",
            category="少儿绘本",
            binding="精装",
            tags=["新书上架", "青少年推荐"],
            price=42.5,
            is_sale=True
        ),
        # 24
        BookModel(
            name="蚯蚓的日记",
            category="少儿绘本",
            binding="平装",
            tags=["畅销书", "限时折扣"],
            price=28.9,
            is_sale=True
        ),
        # 25
        BookModel(
            name="逃家小兔",
            category="少儿绘本",
            binding="线装",
            tags=["经典名著", "青少年推荐"],
            price=39.9,
            is_sale=False
        ),
        # 26
        BookModel(
            name="JavaScript高级程序设计",
            category="计算机技术",
            binding="精装",
            tags=["畅销书", "经典名著"],
            price=119.0,
            is_sale=True
        ),
        # 27
        BookModel(
            name="红楼梦",
            category="文学小说",
            binding="线装",
            tags=["经典名著", "畅销书"],
            price=198.0,
            is_sale=True
        ),
        # 28
        BookModel(
            name="物种起源",
            category="科普读物",
            binding="精装",
            tags=["经典名著", "青少年推荐"],
            price=72.5,
            is_sale=True
        ),
        # 29
        BookModel(
            name="史记",
            category="历史传记",
            binding="线装",
            tags=["经典名著"],
            price=268.0,
            is_sale=False
        ),
        # 30
        BookModel(
            name="金字塔原理",
            category="人文社科",
            binding="平装",
            tags=["畅销书", "新书上架"],
            price=59.9,
            is_sale=True
        )
    ]

    book_service = BookService()
    for book in books:
        book_service.save(book)
