# Generated from c:\Users\HP\Desktop\PPL\assignment1\src\main\d96\parser\D96.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3H")
        buf.write("\u0246\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\3\2\6\2n\n\2\r\2\16\2o\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3x\n\3\3\3\3\3\7\3|\n\3\f\3\16\3\177")
        buf.write("\13\3\3\3\5\3\u0082\n\3\3\3\7\3\u0085\n\3\f\3\16\3\u0088")
        buf.write("\13\3\3\3\3\3\3\4\3\4\3\4\5\4\u008f\n\4\3\5\3\5\5\5\u0093")
        buf.write("\n\5\3\6\3\6\3\6\3\6\7\6\u0099\n\6\f\6\16\6\u009c\13\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00b2\n\b\3\t\3\t\3\t\5")
        buf.write("\t\u00b7\n\t\3\t\3\t\3\t\3\n\3\n\3\n\7\n\u00bf\n\n\f\n")
        buf.write("\16\n\u00c2\13\n\3\13\3\13\3\13\7\13\u00c7\n\13\f\13\16")
        buf.write("\13\u00ca\13\13\3\13\3\13\3\13\3\f\3\f\3\f\5\f\u00d2\n")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\7\16\u00de")
        buf.write("\n\16\f\16\16\16\u00e1\13\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\5\17\u00ed\n\17\3\20\3\20\5")
        buf.write("\20\u00f1\n\20\3\21\3\21\3\21\6\21\u00f6\n\21\r\21\16")
        buf.write("\21\u00f7\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\7\22\u0107\n\22\f\22\16\22\u010a")
        buf.write("\13\22\3\22\3\22\5\22\u010e\n\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u0119\n\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\5\26\u0126\n")
        buf.write("\26\3\26\3\26\3\27\3\27\5\27\u012c\n\27\3\30\3\30\5\30")
        buf.write("\u0130\n\30\3\31\3\31\5\31\u0134\n\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\7\31\u013c\n\31\f\31\16\31\u013f\13\31\5")
        buf.write("\31\u0141\n\31\3\31\3\31\5\31\u0145\n\31\3\32\3\32\5\32")
        buf.write("\u0149\n\32\3\32\3\32\3\32\3\32\3\32\3\32\7\32\u0151\n")
        buf.write("\32\f\32\16\32\u0154\13\32\5\32\u0156\n\32\3\32\3\32\5")
        buf.write("\32\u015a\n\32\3\33\3\33\5\33\u015e\n\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\5\35\u0168\n\35\3\35\3\35\3")
        buf.write("\35\3\36\3\36\3\36\3\36\7\36\u0171\n\36\f\36\16\36\u0174")
        buf.write("\13\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \5 \u018a\n \3!\3!\3!\5!\u018f")
        buf.write("\n!\3\"\3\"\3#\3#\3#\3#\3#\5#\u0198\n#\3#\3#\3#\3#\3$")
        buf.write("\3$\3%\3%\3%\3%\3%\3%\7%\u01a6\n%\f%\16%\u01a9\13%\5%")
        buf.write("\u01ab\n%\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3(\6(\u01b7\n(")
        buf.write("\r(\16(\u01b8\3)\3)\3)\3)\3)\5)\u01c0\n)\3*\3*\3*\3*\3")
        buf.write("*\5*\u01c7\n*\3+\3+\3+\3+\3+\3+\7+\u01cf\n+\f+\16+\u01d2")
        buf.write("\13+\3,\3,\3,\3,\3,\3,\7,\u01da\n,\f,\16,\u01dd\13,\3")
        buf.write("-\3-\3-\3-\3-\3-\7-\u01e5\n-\f-\16-\u01e8\13-\3.\3.\3")
        buf.write(".\5.\u01ed\n.\3/\3/\3/\5/\u01f2\n/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\7\60\u01f9\n\60\f\60\16\60\u01fc\13\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u0204\n\61\f\61\16\61\u0207")
        buf.write("\13\61\3\62\3\62\3\62\3\62\3\62\5\62\u020e\n\62\3\63\3")
        buf.write("\63\3\63\5\63\u0213\n\63\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64\u0222\n\64\3")
        buf.write("\65\3\65\3\65\7\65\u0227\n\65\f\65\16\65\u022a\13\65\3")
        buf.write("\65\3\65\3\65\3\65\3\65\7\65\u0231\n\65\f\65\16\65\u0234")
        buf.write("\13\65\3\65\3\65\5\65\u0238\n\65\3\66\3\66\3\66\3\66\3")
        buf.write("\66\7\66\u023f\n\66\f\66\16\66\u0242\13\66\3\66\3\66\3")
        buf.write("\66\2\7TVX^`\67\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36")
        buf.write(" \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhj\2\13")
        buf.write("\3\2 !\3\2DE\4\2\16\16\20\22\4\2\3\5\n\13\3\2\66\67\4")
        buf.write("\2//\61\65\3\2-.\3\2\'(\3\2)+\2\u0259\2m\3\2\2\2\4s\3")
        buf.write("\2\2\2\6\u008e\3\2\2\2\b\u0092\3\2\2\2\n\u0094\3\2\2\2")
        buf.write("\f\u00a1\3\2\2\2\16\u00b1\3\2\2\2\20\u00b3\3\2\2\2\22")
        buf.write("\u00bb\3\2\2\2\24\u00c3\3\2\2\2\26\u00ce\3\2\2\2\30\u00d6")
        buf.write("\3\2\2\2\32\u00db\3\2\2\2\34\u00ec\3\2\2\2\36\u00f0\3")
        buf.write("\2\2\2 \u00f2\3\2\2\2\"\u00fb\3\2\2\2$\u010f\3\2\2\2&")
        buf.write("\u011d\3\2\2\2(\u0120\3\2\2\2*\u0123\3\2\2\2,\u012b\3")
        buf.write("\2\2\2.\u012f\3\2\2\2\60\u0133\3\2\2\2\62\u0148\3\2\2")
        buf.write("\2\64\u015d\3\2\2\2\66\u015f\3\2\2\28\u0167\3\2\2\2:\u016c")
        buf.write("\3\2\2\2<\u0179\3\2\2\2>\u0189\3\2\2\2@\u018e\3\2\2\2")
        buf.write("B\u0190\3\2\2\2D\u0192\3\2\2\2F\u019d\3\2\2\2H\u019f\3")
        buf.write("\2\2\2J\u01ae\3\2\2\2L\u01b0\3\2\2\2N\u01b6\3\2\2\2P\u01bf")
        buf.write("\3\2\2\2R\u01c6\3\2\2\2T\u01c8\3\2\2\2V\u01d3\3\2\2\2")
        buf.write("X\u01de\3\2\2\2Z\u01ec\3\2\2\2\\\u01f1\3\2\2\2^\u01f3")
        buf.write("\3\2\2\2`\u01fd\3\2\2\2b\u020d\3\2\2\2d\u0212\3\2\2\2")
        buf.write("f\u0221\3\2\2\2h\u0237\3\2\2\2j\u0239\3\2\2\2ln\5\4\3")
        buf.write("\2ml\3\2\2\2no\3\2\2\2om\3\2\2\2op\3\2\2\2pq\3\2\2\2q")
        buf.write("r\7\2\2\3r\3\3\2\2\2st\7\37\2\2tw\5L\'\2uv\7C\2\2vx\5")
        buf.write("L\'\2wu\3\2\2\2wx\3\2\2\2xy\3\2\2\2y}\7=\2\2z|\5\6\4\2")
        buf.write("{z\3\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\u0081\3\2")
        buf.write("\2\2\177}\3\2\2\2\u0080\u0082\5\30\r\2\u0081\u0080\3\2")
        buf.write("\2\2\u0081\u0082\3\2\2\2\u0082\u0086\3\2\2\2\u0083\u0085")
        buf.write("\5\6\4\2\u0084\u0083\3\2\2\2\u0085\u0088\3\2\2\2\u0086")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0089\3\2\2\2")
        buf.write("\u0088\u0086\3\2\2\2\u0089\u008a\7>\2\2\u008a\5\3\2\2")
        buf.write("\2\u008b\u008f\5\b\5\2\u008c\u008f\5\20\t\2\u008d\u008f")
        buf.write("\5\26\f\2\u008e\u008b\3\2\2\2\u008e\u008c\3\2\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008f\7\3\2\2\2\u0090\u0093\5\n\6\2\u0091")
        buf.write("\u0093\5\f\7\2\u0092\u0090\3\2\2\2\u0092\u0091\3\2\2\2")
        buf.write("\u0093\t\3\2\2\2\u0094\u0095\t\2\2\2\u0095\u009a\5L\'")
        buf.write("\2\u0096\u0097\7A\2\2\u0097\u0099\5L\'\2\u0098\u0096\3")
        buf.write("\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b")
        buf.write("\3\2\2\2\u009b\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d")
        buf.write("\u009e\7C\2\2\u009e\u009f\5@!\2\u009f\u00a0\7B\2\2\u00a0")
        buf.write("\13\3\2\2\2\u00a1\u00a2\t\2\2\2\u00a2\u00a3\5\16\b\2\u00a3")
        buf.write("\u00a4\7B\2\2\u00a4\r\3\2\2\2\u00a5\u00a6\5L\'\2\u00a6")
        buf.write("\u00a7\7C\2\2\u00a7\u00a8\5@!\2\u00a8\u00a9\7\60\2\2\u00a9")
        buf.write("\u00aa\5P)\2\u00aa\u00b2\3\2\2\2\u00ab\u00ac\5L\'\2\u00ac")
        buf.write("\u00ad\7A\2\2\u00ad\u00ae\5\16\b\2\u00ae\u00af\7A\2\2")
        buf.write("\u00af\u00b0\5P)\2\u00b0\u00b2\3\2\2\2\u00b1\u00a5\3\2")
        buf.write("\2\2\u00b1\u00ab\3\2\2\2\u00b2\17\3\2\2\2\u00b3\u00b4")
        buf.write("\5L\'\2\u00b4\u00b6\79\2\2\u00b5\u00b7\5\22\n\2\u00b6")
        buf.write("\u00b5\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b8\3\2\2\2")
        buf.write("\u00b8\u00b9\7:\2\2\u00b9\u00ba\5\32\16\2\u00ba\21\3\2")
        buf.write("\2\2\u00bb\u00c0\5\24\13\2\u00bc\u00bd\7B\2\2\u00bd\u00bf")
        buf.write("\5\24\13\2\u00be\u00bc\3\2\2\2\u00bf\u00c2\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\23\3\2\2\2\u00c2")
        buf.write("\u00c0\3\2\2\2\u00c3\u00c8\5L\'\2\u00c4\u00c5\7A\2\2\u00c5")
        buf.write("\u00c7\5L\'\2\u00c6\u00c4\3\2\2\2\u00c7\u00ca\3\2\2\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3")
        buf.write("\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00cc\7C\2\2\u00cc\u00cd")
        buf.write("\5@!\2\u00cd\25\3\2\2\2\u00ce\u00cf\7\"\2\2\u00cf\u00d1")
        buf.write("\79\2\2\u00d0\u00d2\5\22\n\2\u00d1\u00d0\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\7:\2\2")
        buf.write("\u00d4\u00d5\5\32\16\2\u00d5\27\3\2\2\2\u00d6\u00d7\7")
        buf.write("#\2\2\u00d7\u00d8\79\2\2\u00d8\u00d9\7:\2\2\u00d9\u00da")
        buf.write("\5\32\16\2\u00da\31\3\2\2\2\u00db\u00df\7=\2\2\u00dc\u00de")
        buf.write("\5\34\17\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df")
        buf.write("\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00e2\3\2\2\2")
        buf.write("\u00e1\u00df\3\2\2\2\u00e2\u00e3\7>\2\2\u00e3\33\3\2\2")
        buf.write("\2\u00e4\u00ed\5\36\20\2\u00e5\u00ed\5 \21\2\u00e6\u00ed")
        buf.write("\5\"\22\2\u00e7\u00ed\5$\23\2\u00e8\u00ed\5&\24\2\u00e9")
        buf.write("\u00ed\5(\25\2\u00ea\u00ed\5*\26\2\u00eb\u00ed\5,\27\2")
        buf.write("\u00ec\u00e4\3\2\2\2\u00ec\u00e5\3\2\2\2\u00ec\u00e6\3")
        buf.write("\2\2\2\u00ec\u00e7\3\2\2\2\u00ec\u00e8\3\2\2\2\u00ec\u00e9")
        buf.write("\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed")
        buf.write("\35\3\2\2\2\u00ee\u00f1\5:\36\2\u00ef\u00f1\5<\37\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\37\3\2\2\2\u00f2")
        buf.write("\u00f5\5P)\2\u00f3\u00f4\7\60\2\2\u00f4\u00f6\5P)\2\u00f5")
        buf.write("\u00f3\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f5\3\2\2\2")
        buf.write("\u00f7\u00f8\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\7")
        buf.write("B\2\2\u00fa!\3\2\2\2\u00fb\u00fc\7\26\2\2\u00fc\u00fd")
        buf.write("\79\2\2\u00fd\u00fe\5P)\2\u00fe\u00ff\7:\2\2\u00ff\u0108")
        buf.write("\5\32\16\2\u0100\u0101\7\27\2\2\u0101\u0102\79\2\2\u0102")
        buf.write("\u0103\5P)\2\u0103\u0104\7:\2\2\u0104\u0105\5\32\16\2")
        buf.write("\u0105\u0107\3\2\2\2\u0106\u0100\3\2\2\2\u0107\u010a\3")
        buf.write("\2\2\2\u0108\u0106\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010d")
        buf.write("\3\2\2\2\u010a\u0108\3\2\2\2\u010b\u010c\7\30\2\2\u010c")
        buf.write("\u010e\5\32\16\2\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2")
        buf.write("\2\u010e#\3\2\2\2\u010f\u0110\7\31\2\2\u0110\u0111\79")
        buf.write("\2\2\u0111\u0112\7D\2\2\u0112\u0113\7\35\2\2\u0113\u0114")
        buf.write("\5P)\2\u0114\u0115\7@\2\2\u0115\u0118\5P)\2\u0116\u0117")
        buf.write("\7%\2\2\u0117\u0119\5P)\2\u0118\u0116\3\2\2\2\u0118\u0119")
        buf.write("\3\2\2\2\u0119\u011a\3\2\2\2\u011a\u011b\7:\2\2\u011b")
        buf.write("\u011c\5\32\16\2\u011c%\3\2\2\2\u011d\u011e\7\24\2\2\u011e")
        buf.write("\u011f\7B\2\2\u011f\'\3\2\2\2\u0120\u0121\7\25\2\2\u0121")
        buf.write("\u0122\7B\2\2\u0122)\3\2\2\2\u0123\u0125\7\23\2\2\u0124")
        buf.write("\u0126\5P)\2\u0125\u0124\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0128\7B\2\2\u0128+\3\2\2\2\u0129")
        buf.write("\u012c\5\60\31\2\u012a\u012c\5\62\32\2\u012b\u0129\3\2")
        buf.write("\2\2\u012b\u012a\3\2\2\2\u012c-\3\2\2\2\u012d\u0130\5")
        buf.write("\60\31\2\u012e\u0130\5\62\32\2\u012f\u012d\3\2\2\2\u012f")
        buf.write("\u012e\3\2\2\2\u0130/\3\2\2\2\u0131\u0134\5L\'\2\u0132")
        buf.write("\u0134\7&\2\2\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135\u0136\7?\2\2\u0136\u0137\7")
        buf.write("D\2\2\u0137\u0140\79\2\2\u0138\u013d\5P)\2\u0139\u013a")
        buf.write("\7A\2\2\u013a\u013c\5P)\2\u013b\u0139\3\2\2\2\u013c\u013f")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013d\u013e\3\2\2\2\u013e")
        buf.write("\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u0140\u0138\3\2\2\2")
        buf.write("\u0140\u0141\3\2\2\2\u0141\u0142\3\2\2\2\u0142\u0144\7")
        buf.write(":\2\2\u0143\u0145\7B\2\2\u0144\u0143\3\2\2\2\u0144\u0145")
        buf.write("\3\2\2\2\u0145\61\3\2\2\2\u0146\u0149\5L\'\2\u0147\u0149")
        buf.write("\7&\2\2\u0148\u0146\3\2\2\2\u0148\u0147\3\2\2\2\u0149")
        buf.write("\u014a\3\2\2\2\u014a\u014b\78\2\2\u014b\u014c\7E\2\2\u014c")
        buf.write("\u0155\79\2\2\u014d\u0152\5P)\2\u014e\u014f\7A\2\2\u014f")
        buf.write("\u0151\5P)\2\u0150\u014e\3\2\2\2\u0151\u0154\3\2\2\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0156\3\2\2\2")
        buf.write("\u0154\u0152\3\2\2\2\u0155\u014d\3\2\2\2\u0155\u0156\3")
        buf.write("\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159\7:\2\2\u0158\u015a")
        buf.write("\7B\2\2\u0159\u0158\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\63\3\2\2\2\u015b\u015e\5\66\34\2\u015c\u015e\58\35\2")
        buf.write("\u015d\u015b\3\2\2\2\u015d\u015c\3\2\2\2\u015e\65\3\2")
        buf.write("\2\2\u015f\u0160\5P)\2\u0160\u0161\7?\2\2\u0161\u0162")
        buf.write("\7D\2\2\u0162\67\3\2\2\2\u0163\u0168\5L\'\2\u0164\u0168")
        buf.write("\7&\2\2\u0165\u0166\t\3\2\2\u0166\u0168\5N(\2\u0167\u0163")
        buf.write("\3\2\2\2\u0167\u0164\3\2\2\2\u0167\u0165\3\2\2\2\u0168")
        buf.write("\u0169\3\2\2\2\u0169\u016a\78\2\2\u016a\u016b\7E\2\2\u016b")
        buf.write("9\3\2\2\2\u016c\u016d\t\2\2\2\u016d\u0172\7D\2\2\u016e")
        buf.write("\u016f\7A\2\2\u016f\u0171\7D\2\2\u0170\u016e\3\2\2\2\u0171")
        buf.write("\u0174\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0175\3\2\2\2\u0174\u0172\3\2\2\2\u0175\u0176\7")
        buf.write("C\2\2\u0176\u0177\5@!\2\u0177\u0178\7B\2\2\u0178;\3\2")
        buf.write("\2\2\u0179\u017a\t\2\2\2\u017a\u017b\5> \2\u017b\u017c")
        buf.write("\7B\2\2\u017c=\3\2\2\2\u017d\u017e\7D\2\2\u017e\u017f")
        buf.write("\7C\2\2\u017f\u0180\5@!\2\u0180\u0181\7\60\2\2\u0181\u0182")
        buf.write("\5P)\2\u0182\u018a\3\2\2\2\u0183\u0184\7D\2\2\u0184\u0185")
        buf.write("\7A\2\2\u0185\u0186\5> \2\u0186\u0187\7A\2\2\u0187\u0188")
        buf.write("\5P)\2\u0188\u018a\3\2\2\2\u0189\u017d\3\2\2\2\u0189\u0183")
        buf.write("\3\2\2\2\u018a?\3\2\2\2\u018b\u018f\5B\"\2\u018c\u018f")
        buf.write("\5D#\2\u018d\u018f\5F$\2\u018e\u018b\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018e\u018d\3\2\2\2\u018fA\3\2\2\2\u0190\u0191")
        buf.write("\t\4\2\2\u0191C\3\2\2\2\u0192\u0193\7\34\2\2\u0193\u0197")
        buf.write("\7;\2\2\u0194\u0198\5B\"\2\u0195\u0198\5D#\2\u0196\u0198")
        buf.write("\5F$\2\u0197\u0194\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0196")
        buf.write("\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\7A\2\2\u019a")
        buf.write("\u019b\7\4\2\2\u019b\u019c\7<\2\2\u019cE\3\2\2\2\u019d")
        buf.write("\u019e\7D\2\2\u019eG\3\2\2\2\u019f\u01a0\7$\2\2\u01a0")
        buf.write("\u01a1\7D\2\2\u01a1\u01aa\79\2\2\u01a2\u01a7\5P)\2\u01a3")
        buf.write("\u01a4\7A\2\2\u01a4\u01a6\5P)\2\u01a5\u01a3\3\2\2\2\u01a6")
        buf.write("\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01a2\3")
        buf.write("\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ad")
        buf.write("\7:\2\2\u01adI\3\2\2\2\u01ae\u01af\t\5\2\2\u01afK\3\2")
        buf.write("\2\2\u01b0\u01b1\t\3\2\2\u01b1M\3\2\2\2\u01b2\u01b3\7")
        buf.write(";\2\2\u01b3\u01b4\5P)\2\u01b4\u01b5\7<\2\2\u01b5\u01b7")
        buf.write("\3\2\2\2\u01b6\u01b2\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9O\3\2\2\2\u01ba")
        buf.write("\u01bb\5R*\2\u01bb\u01bc\t\6\2\2\u01bc\u01bd\5R*\2\u01bd")
        buf.write("\u01c0\3\2\2\2\u01be\u01c0\5R*\2\u01bf\u01ba\3\2\2\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01c0Q\3\2\2\2\u01c1\u01c2\5T+\2\u01c2")
        buf.write("\u01c3\t\7\2\2\u01c3\u01c4\5T+\2\u01c4\u01c7\3\2\2\2\u01c5")
        buf.write("\u01c7\5T+\2\u01c6\u01c1\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7")
        buf.write("S\3\2\2\2\u01c8\u01c9\b+\1\2\u01c9\u01ca\5V,\2\u01ca\u01d0")
        buf.write("\3\2\2\2\u01cb\u01cc\f\4\2\2\u01cc\u01cd\t\b\2\2\u01cd")
        buf.write("\u01cf\5V,\2\u01ce\u01cb\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1U\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d3\u01d4\b,\1\2\u01d4\u01d5\5X-\2\u01d5")
        buf.write("\u01db\3\2\2\2\u01d6\u01d7\f\4\2\2\u01d7\u01d8\t\t\2\2")
        buf.write("\u01d8\u01da\5X-\2\u01d9\u01d6\3\2\2\2\u01da\u01dd\3\2")
        buf.write("\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dcW\3")
        buf.write("\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01df\b-\1\2\u01df\u01e0")
        buf.write("\5Z.\2\u01e0\u01e6\3\2\2\2\u01e1\u01e2\f\4\2\2\u01e2\u01e3")
        buf.write("\t\n\2\2\u01e3\u01e5\5Z.\2\u01e4\u01e1\3\2\2\2\u01e5\u01e8")
        buf.write("\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7")
        buf.write("Y\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01ea\7,\2\2\u01ea")
        buf.write("\u01ed\5Z.\2\u01eb\u01ed\5\\/\2\u01ec\u01e9\3\2\2\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed[\3\2\2\2\u01ee\u01ef\7(\2\2\u01ef")
        buf.write("\u01f2\5\\/\2\u01f0\u01f2\5^\60\2\u01f1\u01ee\3\2\2\2")
        buf.write("\u01f1\u01f0\3\2\2\2\u01f2]\3\2\2\2\u01f3\u01f4\b\60\1")
        buf.write("\2\u01f4\u01f5\5`\61\2\u01f5\u01fa\3\2\2\2\u01f6\u01f7")
        buf.write("\f\4\2\2\u01f7\u01f9\5N(\2\u01f8\u01f6\3\2\2\2\u01f9\u01fc")
        buf.write("\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb")
        buf.write("_\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd\u01fe\b\61\1\2\u01fe")
        buf.write("\u01ff\5b\62\2\u01ff\u0205\3\2\2\2\u0200\u0201\f\4\2\2")
        buf.write("\u0201\u0202\7?\2\2\u0202\u0204\5b\62\2\u0203\u0200\3")
        buf.write("\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206")
        buf.write("\3\2\2\2\u0206a\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u0209")
        buf.write("\5d\63\2\u0209\u020a\78\2\2\u020a\u020b\5d\63\2\u020b")
        buf.write("\u020e\3\2\2\2\u020c\u020e\5d\63\2\u020d\u0208\3\2\2\2")
        buf.write("\u020d\u020c\3\2\2\2\u020ec\3\2\2\2\u020f\u0210\7$\2\2")
        buf.write("\u0210\u0213\5d\63\2\u0211\u0213\5f\64\2\u0212\u020f\3")
        buf.write("\2\2\2\u0212\u0211\3\2\2\2\u0213e\3\2\2\2\u0214\u0222")
        buf.write("\5J&\2\u0215\u0222\5.\30\2\u0216\u0222\7&\2\2\u0217\u0218")
        buf.write("\t\3\2\2\u0218\u0222\5N(\2\u0219\u0222\5j\66\2\u021a\u0222")
        buf.write("\7\36\2\2\u021b\u0222\5H%\2\u021c\u0222\5L\'\2\u021d\u021e")
        buf.write("\79\2\2\u021e\u021f\5P)\2\u021f\u0220\7:\2\2\u0220\u0222")
        buf.write("\3\2\2\2\u0221\u0214\3\2\2\2\u0221\u0215\3\2\2\2\u0221")
        buf.write("\u0216\3\2\2\2\u0221\u0217\3\2\2\2\u0221\u0219\3\2\2\2")
        buf.write("\u0221\u021a\3\2\2\2\u0221\u021b\3\2\2\2\u0221\u021c\3")
        buf.write("\2\2\2\u0221\u021d\3\2\2\2\u0222g\3\2\2\2\u0223\u0228")
        buf.write("\5j\66\2\u0224\u0225\7A\2\2\u0225\u0227\5j\66\2\u0226")
        buf.write("\u0224\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229\u0238\3\2\2\2\u022a\u0228\3")
        buf.write("\2\2\2\u022b\u022c\7\34\2\2\u022c\u022d\79\2\2\u022d\u0232")
        buf.write("\5h\65\2\u022e\u022f\7A\2\2\u022f\u0231\5h\65\2\u0230")
        buf.write("\u022e\3\2\2\2\u0231\u0234\3\2\2\2\u0232\u0230\3\2\2\2")
        buf.write("\u0232\u0233\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0232\3")
        buf.write("\2\2\2\u0235\u0236\7:\2\2\u0236\u0238\3\2\2\2\u0237\u0223")
        buf.write("\3\2\2\2\u0237\u022b\3\2\2\2\u0238i\3\2\2\2\u0239\u023a")
        buf.write("\7\34\2\2\u023a\u023b\79\2\2\u023b\u0240\5P)\2\u023c\u023d")
        buf.write("\7A\2\2\u023d\u023f\5P)\2\u023e\u023c\3\2\2\2\u023f\u0242")
        buf.write("\3\2\2\2\u0240\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241")
        buf.write("\u0243\3\2\2\2\u0242\u0240\3\2\2\2\u0243\u0244\7:\2\2")
        buf.write("\u0244k\3\2\2\2:ow}\u0081\u0086\u008e\u0092\u009a\u00b1")
        buf.write("\u00b6\u00c0\u00c8\u00d1\u00df\u00ec\u00f0\u00f7\u0108")
        buf.write("\u010d\u0118\u0125\u012b\u012f\u0133\u013d\u0140\u0144")
        buf.write("\u0148\u0152\u0155\u0159\u015d\u0167\u0172\u0189\u018e")
        buf.write("\u0197\u01a7\u01aa\u01b8\u01bf\u01c6\u01d0\u01db\u01e6")
        buf.write("\u01ec\u01f1\u01fa\u0205\u020d\u0212\u0221\u0228\u0232")
        buf.write("\u0237\u0240")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Int'", "'Void'", "'Float'", "'String'", "'Boolean'", 
                     "'Return'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
                     "'In'", "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
                     "'Destructor'", "'New'", "'By'", "'Self'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'+.'", 
                     "'==.'", "'::'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'.'", "'..'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "BOOLEAN_LITERAL", "NATURAL", "INTEGER_LIERAL", 
                      "DECIMAL", "BINARY", "OCTAL", "HEXADECIMAL", "FLOAT_LITERAL", 
                      "STRING_LITERAL", "WS", "BLOCK_COMMENT", "INT_TYPE", 
                      "VOID_TYPE", "FLOAT_TYPE", "STRING_TYPE", "BOOLEAN_TYPE", 
                      "RETURN", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                      "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "NULL", 
                      "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", 
                      "NOT", "AND", "OR", "EQUAL", "ASSIGN", "NOT_EQUAL", 
                      "LESS_THAN", "LESS_THAN_EQUAL", "GREATER_THAN", "GREATER_THAN_EQUAL", 
                      "STRING_CONCATE", "STRING_COMPARE", "STATIC_GLOBAL_DOT", 
                      "LP", "RP", "LSB", "RSB", "LCB", "RCB", "DOT", "DOUBLEDOT", 
                      "COMMA", "SEMI", "COLON", "ID", "DOLLAR_ID", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_decl = 1
    RULE_member_list = 2
    RULE_attribute_decl = 3
    RULE_attribute_decl_1 = 4
    RULE_attribute_decl_2 = 5
    RULE_attribute_testing = 6
    RULE_method_decl = 7
    RULE_parameter_list = 8
    RULE_parameter = 9
    RULE_constructor = 10
    RULE_destructor = 11
    RULE_block_statement = 12
    RULE_statement = 13
    RULE_var_const_decl_statement = 14
    RULE_assign_statement = 15
    RULE_if_statement = 16
    RULE_for_statement = 17
    RULE_break_statement = 18
    RULE_continue_statement = 19
    RULE_return_statement = 20
    RULE_method_invocate_statement = 21
    RULE_method_invocate_expression = 22
    RULE_instance_method_invocate = 23
    RULE_static_method_invocate = 24
    RULE_attribute_access = 25
    RULE_instance_attribute_access = 26
    RULE_static_attribute_access = 27
    RULE_var_const_decl_1 = 28
    RULE_var_const_decl_2 = 29
    RULE_var_const_testing = 30
    RULE_data_types = 31
    RULE_primitive_types = 32
    RULE_array_type = 33
    RULE_class_type = 34
    RULE_class_new_object = 35
    RULE_literals = 36
    RULE_identifier = 37
    RULE_index_id = 38
    RULE_expr = 39
    RULE_expr_1 = 40
    RULE_expr_2 = 41
    RULE_expr_3 = 42
    RULE_expr_4 = 43
    RULE_expr_5 = 44
    RULE_expr_6 = 45
    RULE_expr_7 = 46
    RULE_expr_8 = 47
    RULE_expr_9 = 48
    RULE_expr_10 = 49
    RULE_expr_11 = 50
    RULE_multi_dimensional_arrays = 51
    RULE_indexed_array = 52

    ruleNames =  [ "program", "class_decl", "member_list", "attribute_decl", 
                   "attribute_decl_1", "attribute_decl_2", "attribute_testing", 
                   "method_decl", "parameter_list", "parameter", "constructor", 
                   "destructor", "block_statement", "statement", "var_const_decl_statement", 
                   "assign_statement", "if_statement", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "method_invocate_statement", "method_invocate_expression", 
                   "instance_method_invocate", "static_method_invocate", 
                   "attribute_access", "instance_attribute_access", "static_attribute_access", 
                   "var_const_decl_1", "var_const_decl_2", "var_const_testing", 
                   "data_types", "primitive_types", "array_type", "class_type", 
                   "class_new_object", "literals", "identifier", "index_id", 
                   "expr", "expr_1", "expr_2", "expr_3", "expr_4", "expr_5", 
                   "expr_6", "expr_7", "expr_8", "expr_9", "expr_10", "expr_11", 
                   "multi_dimensional_arrays", "indexed_array" ]

    EOF = Token.EOF
    BOOLEAN_LITERAL=1
    NATURAL=2
    INTEGER_LIERAL=3
    DECIMAL=4
    BINARY=5
    OCTAL=6
    HEXADECIMAL=7
    FLOAT_LITERAL=8
    STRING_LITERAL=9
    WS=10
    BLOCK_COMMENT=11
    INT_TYPE=12
    VOID_TYPE=13
    FLOAT_TYPE=14
    STRING_TYPE=15
    BOOLEAN_TYPE=16
    RETURN=17
    BREAK=18
    CONTINUE=19
    IF=20
    ELSEIF=21
    ELSE=22
    FOREACH=23
    TRUE=24
    FALSE=25
    ARRAY=26
    IN=27
    NULL=28
    CLASS=29
    VAL=30
    VAR=31
    CONSTRUCTOR=32
    DESTRUCTOR=33
    NEW=34
    BY=35
    SELF=36
    ADD=37
    SUB=38
    MUL=39
    DIV=40
    MOD=41
    NOT=42
    AND=43
    OR=44
    EQUAL=45
    ASSIGN=46
    NOT_EQUAL=47
    LESS_THAN=48
    LESS_THAN_EQUAL=49
    GREATER_THAN=50
    GREATER_THAN_EQUAL=51
    STRING_CONCATE=52
    STRING_COMPARE=53
    STATIC_GLOBAL_DOT=54
    LP=55
    RP=56
    LSB=57
    RSB=58
    LCB=59
    RCB=60
    DOT=61
    DOUBLEDOT=62
    COMMA=63
    SEMI=64
    COLON=65
    ID=66
    DOLLAR_ID=67
    UNCLOSE_STRING=68
    ILLEGAL_ESCAPE=69
    ERROR_CHAR=70

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def class_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 106
                self.class_decl()
                self.state = 109 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 111
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdentifierContext,i)


        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def member_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Member_listContext)
            else:
                return self.getTypedRuleContext(D96Parser.Member_listContext,i)


        def destructor(self):
            return self.getTypedRuleContext(D96Parser.DestructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_decl




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(D96Parser.CLASS)
            self.state = 114
            self.identifier()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 115
                self.match(D96Parser.COLON)
                self.state = 116
                self.identifier()


            self.state = 119
            self.match(D96Parser.LCB)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 120
                    self.member_list() 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.DESTRUCTOR:
                self.state = 126
                self.destructor()


            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & ((1 << (D96Parser.VAL - 30)) | (1 << (D96Parser.VAR - 30)) | (1 << (D96Parser.CONSTRUCTOR - 30)) | (1 << (D96Parser.ID - 30)) | (1 << (D96Parser.DOLLAR_ID - 30)))) != 0):
                self.state = 129
                self.member_list()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl(self):
            return self.getTypedRuleContext(D96Parser.Attribute_declContext,0)


        def method_decl(self):
            return self.getTypedRuleContext(D96Parser.Method_declContext,0)


        def constructor(self):
            return self.getTypedRuleContext(D96Parser.ConstructorContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_member_list




    def member_list(self):

        localctx = D96Parser.Member_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member_list)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.attribute_decl()
                pass
            elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.method_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.constructor()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl_1(self):
            return self.getTypedRuleContext(D96Parser.Attribute_decl_1Context,0)


        def attribute_decl_2(self):
            return self.getTypedRuleContext(D96Parser.Attribute_decl_2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl




    def attribute_decl(self):

        localctx = D96Parser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_decl)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.attribute_decl_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.attribute_decl_2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_decl_1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdentifierContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_types(self):
            return self.getTypedRuleContext(D96Parser.Data_typesContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl_1




    def attribute_decl_1(self):

        localctx = D96Parser.Attribute_decl_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_decl_1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 147
            self.identifier()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 148
                self.match(D96Parser.COMMA)
                self.state = 149
                self.identifier()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
            self.match(D96Parser.COLON)
            self.state = 156
            self.data_types()
            self.state = 157
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_decl_2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_testing(self):
            return self.getTypedRuleContext(D96Parser.Attribute_testingContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl_2




    def attribute_decl_2(self):

        localctx = D96Parser.Attribute_decl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute_decl_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 160
            self.attribute_testing()
            self.state = 161
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_testingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_types(self):
            return self.getTypedRuleContext(D96Parser.Data_typesContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def attribute_testing(self):
            return self.getTypedRuleContext(D96Parser.Attribute_testingContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_testing




    def attribute_testing(self):

        localctx = D96Parser.Attribute_testingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_testing)
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.identifier()
                self.state = 164
                self.match(D96Parser.COLON)
                self.state = 165
                self.data_types()
                self.state = 166
                self.match(D96Parser.ASSIGN)
                self.state = 167
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.identifier()
                self.state = 170
                self.match(D96Parser.COMMA)
                self.state = 171
                self.attribute_testing()

                self.state = 172
                self.match(D96Parser.COMMA)
                self.state = 173
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_decl




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.identifier()
            self.state = 178
            self.match(D96Parser.LP)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 179
                self.parameter_list()


            self.state = 182
            self.match(D96Parser.RP)
            self.state = 183
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ParameterContext)
            else:
                return self.getTypedRuleContext(D96Parser.ParameterContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SEMI)
            else:
                return self.getToken(D96Parser.SEMI, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter_list




    def parameter_list(self):

        localctx = D96Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.parameter()
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 186
                self.match(D96Parser.SEMI)
                self.state = 187
                self.parameter()
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IdentifierContext)
            else:
                return self.getTypedRuleContext(D96Parser.IdentifierContext,i)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_types(self):
            return self.getTypedRuleContext(D96Parser.Data_typesContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_parameter




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.identifier()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 194
                self.match(D96Parser.COMMA)
                self.state = 195
                self.identifier()
                self.state = 200
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 201
            self.match(D96Parser.COLON)
            self.state = 202
            self.data_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def parameter_list(self):
            return self.getTypedRuleContext(D96Parser.Parameter_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 205
            self.match(D96Parser.LP)
            self.state = 207
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 206
                self.parameter_list()


            self.state = 209
            self.match(D96Parser.RP)
            self.state = 210
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(D96Parser.DESTRUCTOR)
            self.state = 213
            self.match(D96Parser.LP)
            self.state = 214
            self.match(D96Parser.RP)
            self.state = 215
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StatementContext)
            else:
                return self.getTypedRuleContext(D96Parser.StatementContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_block_statement




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(D96Parser.LCB)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.RETURN) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 218
                self.statement()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_const_decl_statement(self):
            return self.getTypedRuleContext(D96Parser.Var_const_decl_statementContext,0)


        def assign_statement(self):
            return self.getTypedRuleContext(D96Parser.Assign_statementContext,0)


        def if_statement(self):
            return self.getTypedRuleContext(D96Parser.If_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(D96Parser.For_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(D96Parser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(D96Parser.Return_statementContext,0)


        def method_invocate_statement(self):
            return self.getTypedRuleContext(D96Parser.Method_invocate_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.var_const_decl_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 229
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 230
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 231
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 232
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 233
                self.method_invocate_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_decl_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_const_decl_1(self):
            return self.getTypedRuleContext(D96Parser.Var_const_decl_1Context,0)


        def var_const_decl_2(self):
            return self.getTypedRuleContext(D96Parser.Var_const_decl_2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_const_decl_statement




    def var_const_decl_statement(self):

        localctx = D96Parser.Var_const_decl_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_const_decl_statement)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 236
                self.var_const_decl_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.var_const_decl_2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ASSIGN)
            else:
                return self.getToken(D96Parser.ASSIGN, i)

        def getRuleIndex(self):
            return D96Parser.RULE_assign_statement




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.expr()
            self.state = 243 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 241
                self.match(D96Parser.ASSIGN)
                self.state = 242
                self.expr()
                self.state = 245 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.ASSIGN):
                    break

            self.state = 247
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LP)
            else:
                return self.getToken(D96Parser.LP, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RP(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RP)
            else:
                return self.getToken(D96Parser.RP, i)

        def block_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Block_statementContext)
            else:
                return self.getTypedRuleContext(D96Parser.Block_statementContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_statement




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(D96Parser.IF)
            self.state = 250
            self.match(D96Parser.LP)
            self.state = 251
            self.expr()
            self.state = 252
            self.match(D96Parser.RP)
            self.state = 253
            self.block_statement()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 254
                self.match(D96Parser.ELSEIF)
                self.state = 255
                self.match(D96Parser.LP)
                self.state = 256
                self.expr()
                self.state = 257
                self.match(D96Parser.RP)
                self.state = 258
                self.block_statement()
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 265
                self.match(D96Parser.ELSE)
                self.state = 266
                self.block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DOUBLEDOT(self):
            return self.getToken(D96Parser.DOUBLEDOT, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def block_statement(self):
            return self.getTypedRuleContext(D96Parser.Block_statementContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_for_statement




    def for_statement(self):

        localctx = D96Parser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.match(D96Parser.FOREACH)
            self.state = 270
            self.match(D96Parser.LP)
            self.state = 271
            self.match(D96Parser.ID)
            self.state = 272
            self.match(D96Parser.IN)
            self.state = 273
            self.expr()
            self.state = 274
            self.match(D96Parser.DOUBLEDOT)
            self.state = 275
            self.expr()
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 276
                self.match(D96Parser.BY)
                self.state = 277
                self.expr()


            self.state = 280
            self.match(D96Parser.RP)
            self.state = 281
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(D96Parser.BREAK)
            self.state = 284
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(D96Parser.CONTINUE)
            self.state = 287
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_statement




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(D96Parser.RETURN)
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 290
                self.expr()


            self.state = 293
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocate_statementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invocateContext,0)


        def static_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocateContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocate_statement




    def method_invocate_statement(self):

        localctx = D96Parser.Method_invocate_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_method_invocate_statement)
        try:
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.instance_method_invocate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.static_method_invocate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocate_expressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invocateContext,0)


        def static_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocateContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocate_expression




    def method_invocate_expression(self):

        localctx = D96Parser.Method_invocate_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_method_invocate_expression)
        try:
            self.state = 301
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.instance_method_invocate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.static_method_invocate()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_invocateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_invocate




    def instance_method_invocate(self):

        localctx = D96Parser.Instance_method_invocateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_instance_method_invocate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.state = 303
                self.identifier()
                pass
            elif token in [D96Parser.SELF]:
                self.state = 304
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 307
            self.match(D96Parser.DOT)
            self.state = 308
            self.match(D96Parser.ID)
            self.state = 309
            self.match(D96Parser.LP)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 310
                self.expr()
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 311
                    self.match(D96Parser.COMMA)
                    self.state = 312
                    self.expr()
                    self.state = 317
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 320
            self.match(D96Parser.RP)
            self.state = 322
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 321
                self.match(D96Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invocateContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_GLOBAL_DOT(self):
            return self.getToken(D96Parser.STATIC_GLOBAL_DOT, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_static_method_invocate




    def static_method_invocate(self):

        localctx = D96Parser.Static_method_invocateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_static_method_invocate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.state = 324
                self.identifier()
                pass
            elif token in [D96Parser.SELF]:
                self.state = 325
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 328
            self.match(D96Parser.STATIC_GLOBAL_DOT)
            self.state = 329
            self.match(D96Parser.DOLLAR_ID)
            self.state = 330
            self.match(D96Parser.LP)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 331
                self.expr()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 332
                    self.match(D96Parser.COMMA)
                    self.state = 333
                    self.expr()
                    self.state = 338
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 341
            self.match(D96Parser.RP)
            self.state = 343
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 342
                self.match(D96Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attribute_accessContext,0)


        def static_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attribute_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_access




    def attribute_access(self):

        localctx = D96Parser.Attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_attribute_access)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.instance_attribute_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.static_attribute_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_attribute_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attribute_access




    def instance_attribute_access(self):

        localctx = D96Parser.Instance_attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_instance_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.expr()
            self.state = 350
            self.match(D96Parser.DOT)
            self.state = 351
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attribute_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_GLOBAL_DOT(self):
            return self.getToken(D96Parser.STATIC_GLOBAL_DOT, 0)

        def DOLLAR_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_ID)
            else:
                return self.getToken(D96Parser.DOLLAR_ID, i)

        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def index_id(self):
            return self.getTypedRuleContext(D96Parser.Index_idContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attribute_access




    def static_attribute_access(self):

        localctx = D96Parser.Static_attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_static_attribute_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 353
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 354
                self.match(D96Parser.SELF)
                pass

            elif la_ == 3:
                self.state = 355
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 356
                self.index_id()
                pass


            self.state = 359
            self.match(D96Parser.STATIC_GLOBAL_DOT)
            self.state = 360
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_decl_1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_types(self):
            return self.getTypedRuleContext(D96Parser.Data_typesContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_var_const_decl_1




    def var_const_decl_1(self):

        localctx = D96Parser.Var_const_decl_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_var_const_decl_1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 363
            self.match(D96Parser.ID)
            self.state = 368
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 364
                self.match(D96Parser.COMMA)
                self.state = 365
                self.match(D96Parser.ID)
                self.state = 370
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 371
            self.match(D96Parser.COLON)
            self.state = 372
            self.data_types()
            self.state = 373
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_decl_2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_const_testing(self):
            return self.getTypedRuleContext(D96Parser.Var_const_testingContext,0)


        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_const_decl_2




    def var_const_decl_2(self):

        localctx = D96Parser.Var_const_decl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_var_const_decl_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 376
            self.var_const_testing()
            self.state = 377
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_testingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def data_types(self):
            return self.getTypedRuleContext(D96Parser.Data_typesContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def var_const_testing(self):
            return self.getTypedRuleContext(D96Parser.Var_const_testingContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_const_testing




    def var_const_testing(self):

        localctx = D96Parser.Var_const_testingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_const_testing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 379
                self.match(D96Parser.ID)
                self.state = 380
                self.match(D96Parser.COLON)
                self.state = 381
                self.data_types()
                self.state = 382
                self.match(D96Parser.ASSIGN)
                self.state = 383
                self.expr()
                pass

            elif la_ == 2:
                self.state = 385
                self.match(D96Parser.ID)
                self.state = 386
                self.match(D96Parser.COMMA)
                self.state = 387
                self.var_const_testing()

                self.state = 388
                self.match(D96Parser.COMMA)
                self.state = 389
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_typesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_data_types




    def data_types(self):

        localctx = D96Parser.Data_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_data_types)
        try:
            self.state = 396
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_TYPE, D96Parser.FLOAT_TYPE, D96Parser.STRING_TYPE, D96Parser.BOOLEAN_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(D96Parser.INT_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(D96Parser.FLOAT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(D96Parser.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(D96Parser.BOOLEAN_TYPE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_types




    def primitive_types(self):

        localctx = D96Parser.Primitive_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT_TYPE) | (1 << D96Parser.FLOAT_TYPE) | (1 << D96Parser.STRING_TYPE) | (1 << D96Parser.BOOLEAN_TYPE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def NATURAL(self):
            return self.getToken(D96Parser.NATURAL, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def primitive_types(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typesContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def class_type(self):
            return self.getTypedRuleContext(D96Parser.Class_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(D96Parser.ARRAY)
            self.state = 401
            self.match(D96Parser.LSB)
            self.state = 405
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_TYPE, D96Parser.FLOAT_TYPE, D96Parser.STRING_TYPE, D96Parser.BOOLEAN_TYPE]:
                self.state = 402
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 403
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.state = 404
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 407
            self.match(D96Parser.COMMA)
            self.state = 408
            self.match(D96Parser.NATURAL)
            self.state = 409
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_new_objectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_class_new_object




    def class_new_object(self):

        localctx = D96Parser.Class_new_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_class_new_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(D96Parser.NEW)
            self.state = 414
            self.match(D96Parser.ID)
            self.state = 415
            self.match(D96Parser.LP)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 416
                self.expr()
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 417
                    self.match(D96Parser.COMMA)
                    self.state = 418
                    self.expr()
                    self.state = 423
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 426
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NATURAL(self):
            return self.getToken(D96Parser.NATURAL, 0)

        def INTEGER_LIERAL(self):
            return self.getToken(D96Parser.INTEGER_LIERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(D96Parser.FLOAT_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(D96Parser.BOOLEAN_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(D96Parser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_literals




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier




    def identifier(self):

        localctx = D96Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            _la = self._input.LA(1)
            if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_idContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LSB)
            else:
                return self.getToken(D96Parser.LSB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RSB)
            else:
                return self.getToken(D96Parser.RSB, i)

        def getRuleIndex(self):
            return D96Parser.RULE_index_id




    def index_id(self):

        localctx = D96Parser.Index_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_index_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 432
                    self.match(D96Parser.LSB)
                    self.state = 433
                    self.expr()
                    self.state = 434
                    self.match(D96Parser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 438 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_1Context,i)


        def STRING_CONCATE(self):
            return self.getToken(D96Parser.STRING_CONCATE, 0)

        def STRING_COMPARE(self):
            return self.getToken(D96Parser.STRING_COMPARE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.expr_1()
                self.state = 441
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRING_CONCATE or _la==D96Parser.STRING_COMPARE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 442
                self.expr_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.expr_1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_2Context,i)


        def EQUAL(self):
            return self.getToken(D96Parser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(D96Parser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(D96Parser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(D96Parser.GREATER_THAN, 0)

        def LESS_THAN_EQUAL(self):
            return self.getToken(D96Parser.LESS_THAN_EQUAL, 0)

        def GREATER_THAN_EQUAL(self):
            return self.getToken(D96Parser.GREATER_THAN_EQUAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_1




    def expr_1(self):

        localctx = D96Parser.Expr_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr_1)
        self._la = 0 # Token type
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.expr_2(0)
                self.state = 448
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LESS_THAN_EQUAL) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GREATER_THAN_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 449
                self.expr_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.expr_2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_3(self):
            return self.getTypedRuleContext(D96Parser.Expr_3Context,0)


        def expr_2(self):
            return self.getTypedRuleContext(D96Parser.Expr_2Context,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_2



    def expr_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.expr_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_2)
                    self.state = 457
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 458
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 459
                    self.expr_3(0) 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_4(self):
            return self.getTypedRuleContext(D96Parser.Expr_4Context,0)


        def expr_3(self):
            return self.getTypedRuleContext(D96Parser.Expr_3Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_3



    def expr_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.expr_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 473
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_3)
                    self.state = 468
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 469
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 470
                    self.expr_4(0) 
                self.state = 475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_5(self):
            return self.getTypedRuleContext(D96Parser.Expr_5Context,0)


        def expr_4(self):
            return self.getTypedRuleContext(D96Parser.Expr_4Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_4



    def expr_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.expr_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 484
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_4)
                    self.state = 479
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 480
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 481
                    self.expr_5() 
                self.state = 486
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def expr_5(self):
            return self.getTypedRuleContext(D96Parser.Expr_5Context,0)


        def expr_6(self):
            return self.getTypedRuleContext(D96Parser.Expr_6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_5




    def expr_5(self):

        localctx = D96Parser.Expr_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr_5)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.match(D96Parser.NOT)
                self.state = 488
                self.expr_5()
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL, D96Parser.NATURAL, D96Parser.INTEGER_LIERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
                self.expr_6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def expr_6(self):
            return self.getTypedRuleContext(D96Parser.Expr_6Context,0)


        def expr_7(self):
            return self.getTypedRuleContext(D96Parser.Expr_7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_6




    def expr_6(self):

        localctx = D96Parser.Expr_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr_6)
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(D96Parser.SUB)
                self.state = 493
                self.expr_6()
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL, D96Parser.NATURAL, D96Parser.INTEGER_LIERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.expr_7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_8(self):
            return self.getTypedRuleContext(D96Parser.Expr_8Context,0)


        def expr_7(self):
            return self.getTypedRuleContext(D96Parser.Expr_7Context,0)


        def index_id(self):
            return self.getTypedRuleContext(D96Parser.Index_idContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_7



    def expr_7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr_7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.expr_8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 504
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_7)
                    self.state = 500
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 501
                    self.index_id() 
                self.state = 506
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_9(self):
            return self.getTypedRuleContext(D96Parser.Expr_9Context,0)


        def expr_8(self):
            return self.getTypedRuleContext(D96Parser.Expr_8Context,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_8



    def expr_8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expr_8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.expr_9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 515
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_8)
                    self.state = 510
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 511
                    self.match(D96Parser.DOT)
                    self.state = 512
                    self.expr_9() 
                self.state = 517
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_10(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr_10Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr_10Context,i)


        def STATIC_GLOBAL_DOT(self):
            return self.getToken(D96Parser.STATIC_GLOBAL_DOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_9




    def expr_9(self):

        localctx = D96Parser.Expr_9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr_9)
        try:
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.expr_10()
                self.state = 519
                self.match(D96Parser.STATIC_GLOBAL_DOT)
                self.state = 520
                self.expr_10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.expr_10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def expr_10(self):
            return self.getTypedRuleContext(D96Parser.Expr_10Context,0)


        def expr_11(self):
            return self.getTypedRuleContext(D96Parser.Expr_11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr_10




    def expr_10(self):

        localctx = D96Parser.Expr_10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr_10)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(D96Parser.NEW)
                self.state = 526
                self.expr_10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.expr_11()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_11Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literals(self):
            return self.getTypedRuleContext(D96Parser.LiteralsContext,0)


        def method_invocate_expression(self):
            return self.getTypedRuleContext(D96Parser.Method_invocate_expressionContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def index_id(self):
            return self.getTypedRuleContext(D96Parser.Index_idContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def indexed_array(self):
            return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,0)


        def NULL(self):
            return self.getToken(D96Parser.NULL, 0)

        def class_new_object(self):
            return self.getTypedRuleContext(D96Parser.Class_new_objectContext,0)


        def identifier(self):
            return self.getTypedRuleContext(D96Parser.IdentifierContext,0)


        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr_11




    def expr_11(self):

        localctx = D96Parser.Expr_11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr_11)
        self._la = 0 # Token type
        try:
            self.state = 543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.method_invocate_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 533
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 534
                self.index_id()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 535
                self.indexed_array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 536
                self.match(D96Parser.NULL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 537
                self.class_new_object()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 538
                self.identifier()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 539
                self.match(D96Parser.LP)
                self.state = 540
                self.expr()
                self.state = 541
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_dimensional_arraysContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def indexed_array(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Indexed_arrayContext)
            else:
                return self.getTypedRuleContext(D96Parser.Indexed_arrayContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def multi_dimensional_arrays(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Multi_dimensional_arraysContext)
            else:
                return self.getTypedRuleContext(D96Parser.Multi_dimensional_arraysContext,i)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_multi_dimensional_arrays




    def multi_dimensional_arrays(self):

        localctx = D96Parser.Multi_dimensional_arraysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_multi_dimensional_arrays)
        self._la = 0 # Token type
        try:
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.indexed_array()
                self.state = 550
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 546
                        self.match(D96Parser.COMMA)
                        self.state = 547
                        self.indexed_array() 
                    self.state = 552
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
                self.match(D96Parser.ARRAY)
                self.state = 554
                self.match(D96Parser.LP)
                self.state = 555
                self.multi_dimensional_arrays()
                self.state = 560
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 556
                    self.match(D96Parser.COMMA)
                    self.state = 557
                    self.multi_dimensional_arrays()
                    self.state = 562
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 563
                self.match(D96Parser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Indexed_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LP(self):
            return self.getToken(D96Parser.LP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RP(self):
            return self.getToken(D96Parser.RP, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_indexed_array




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(D96Parser.ARRAY)
            self.state = 568
            self.match(D96Parser.LP)
            self.state = 569
            self.expr()
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 570
                self.match(D96Parser.COMMA)
                self.state = 571
                self.expr()
                self.state = 576
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 577
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[41] = self.expr_2_sempred
        self._predicates[42] = self.expr_3_sempred
        self._predicates[43] = self.expr_4_sempred
        self._predicates[46] = self.expr_7_sempred
        self._predicates[47] = self.expr_8_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_2_sempred(self, localctx:Expr_2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr_3_sempred(self, localctx:Expr_3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr_4_sempred(self, localctx:Expr_4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr_7_sempred(self, localctx:Expr_7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr_8_sempred(self, localctx:Expr_8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




