from _typeshed import Incomplete

from antlr4.BufferedTokenStream import BufferedTokenStream as BufferedTokenStream
from antlr4.Lexer import Lexer as Lexer
from antlr4.Token import Token as Token

class CommonTokenStream(BufferedTokenStream):
    channel: Incomplete
    def __init__(self, lexer: Lexer, channel: int = 0) -> None: ...
    def adjustSeekIndex(self, i: int) -> int: ...
    def LB(self, k: int) -> Token | None: ...
    def LT(self, k: int) -> Token | None: ...
    def getNumberOfOnChannelTokens(self) -> int: ...
