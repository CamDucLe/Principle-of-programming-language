# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\u026c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\6\2r\n\2\r\2")
        buf.write("\16\2s\3\2\3\2\3\3\3\3\3\3\3\3\5\3|\n\3\3\3\3\3\7\3\u0080")
        buf.write("\n\3\f\3\16\3\u0083\13\3\3\3\5\3\u0086\n\3\3\3\7\3\u0089")
        buf.write("\n\3\f\3\16\3\u008c\13\3\3\3\3\3\3\4\3\4\3\4\5\4\u0093")
        buf.write("\n\4\3\5\3\5\5\5\u0097\n\5\3\6\3\6\3\6\3\6\7\6\u009d\n")
        buf.write("\6\f\6\16\6\u00a0\13\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00b6")
        buf.write("\n\b\3\t\3\t\3\t\5\t\u00bb\n\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\7\n\u00c3\n\n\f\n\16\n\u00c6\13\n\3\13\3\13\3\13\7\13")
        buf.write("\u00cb\n\13\f\13\16\13\u00ce\13\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\5\f\u00d6\n\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\7\16\u00e2\n\16\f\16\16\16\u00e5\13\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00f1")
        buf.write("\n\17\3\20\3\20\5\20\u00f5\n\20\3\21\3\21\3\21\6\21\u00fa")
        buf.write("\n\21\r\21\16\21\u00fb\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u010b\n\22\f\22")
        buf.write("\16\22\u010e\13\22\3\22\3\22\5\22\u0112\n\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u011d\n\23\3")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\5\26\u012a\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\7\27\u0135\n\27\f\27\16\27\u0138\13\27\5\27\u013a")
        buf.write("\n\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\7\30\u0146\n\30\f\30\16\30\u0149\13\30\5\30\u014b\n\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\5\31\u0152\n\31\3\32\3\32\5")
        buf.write("\32\u0156\n\32\3\33\3\33\5\33\u015a\n\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\7\33\u0162\n\33\f\33\16\33\u0165\13\33")
        buf.write("\5\33\u0167\n\33\3\33\3\33\5\33\u016b\n\33\3\34\3\34\5")
        buf.write("\34\u016f\n\34\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0177")
        buf.write("\n\34\f\34\16\34\u017a\13\34\5\34\u017c\n\34\3\34\3\34")
        buf.write("\5\34\u0180\n\34\3\35\3\35\5\35\u0184\n\35\3\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\5\37\u018e\n\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \7 \u0197\n \f \16 \u019a\13 \3 \3 \3")
        buf.write(" \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\5\"\u01b0\n\"\3#\3#\3#\5#\u01b5\n#\3$\3$\3")
        buf.write("%\3%\3%\3%\3%\5%\u01be\n%\3%\3%\3%\3%\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\7\'\u01cc\n\'\f\'\16\'\u01cf\13\'\5\'\u01d1")
        buf.write("\n\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3*\6*\u01dd\n*\r*\16")
        buf.write("*\u01de\3+\3+\3+\3+\3+\5+\u01e6\n+\3,\3,\3,\3,\3,\5,\u01ed")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\7-\u01f5\n-\f-\16-\u01f8\13-\3.")
        buf.write("\3.\3.\3.\3.\3.\7.\u0200\n.\f.\16.\u0203\13.\3/\3/\3/")
        buf.write("\3/\3/\3/\7/\u020b\n/\f/\16/\u020e\13/\3\60\3\60\3\60")
        buf.write("\5\60\u0213\n\60\3\61\3\61\3\61\5\61\u0218\n\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\7\62\u021f\n\62\f\62\16\62\u0222\13")
        buf.write("\62\3\63\3\63\3\63\3\63\3\63\3\63\7\63\u022a\n\63\f\63")
        buf.write("\16\63\u022d\13\63\3\64\3\64\3\64\3\64\3\64\5\64\u0234")
        buf.write("\n\64\3\65\3\65\3\65\5\65\u0239\n\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66")
        buf.write("\u0248\n\66\3\67\3\67\3\67\7\67\u024d\n\67\f\67\16\67")
        buf.write("\u0250\13\67\3\67\3\67\3\67\3\67\3\67\7\67\u0257\n\67")
        buf.write("\f\67\16\67\u025a\13\67\3\67\3\67\5\67\u025e\n\67\38\3")
        buf.write("8\38\38\38\78\u0265\n8\f8\168\u0268\138\38\38\38\2\7X")
        buf.write("Z\\bd9\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjln\2\13\3\2 !")
        buf.write("\3\2DE\4\2\16\16\20\22\4\2\3\5\n\13\3\2\66\67\4\2//\61")
        buf.write("\65\3\2-.\3\2\'(\3\2)+\2\u0281\2q\3\2\2\2\4w\3\2\2\2\6")
        buf.write("\u0092\3\2\2\2\b\u0096\3\2\2\2\n\u0098\3\2\2\2\f\u00a5")
        buf.write("\3\2\2\2\16\u00b5\3\2\2\2\20\u00b7\3\2\2\2\22\u00bf\3")
        buf.write("\2\2\2\24\u00c7\3\2\2\2\26\u00d2\3\2\2\2\30\u00da\3\2")
        buf.write("\2\2\32\u00df\3\2\2\2\34\u00f0\3\2\2\2\36\u00f4\3\2\2")
        buf.write("\2 \u00f6\3\2\2\2\"\u00ff\3\2\2\2$\u0113\3\2\2\2&\u0121")
        buf.write("\3\2\2\2(\u0124\3\2\2\2*\u0127\3\2\2\2,\u012d\3\2\2\2")
        buf.write(".\u013e\3\2\2\2\60\u0151\3\2\2\2\62\u0155\3\2\2\2\64\u0159")
        buf.write("\3\2\2\2\66\u016e\3\2\2\28\u0183\3\2\2\2:\u0185\3\2\2")
        buf.write("\2<\u018d\3\2\2\2>\u0192\3\2\2\2@\u019f\3\2\2\2B\u01af")
        buf.write("\3\2\2\2D\u01b4\3\2\2\2F\u01b6\3\2\2\2H\u01b8\3\2\2\2")
        buf.write("J\u01c3\3\2\2\2L\u01c5\3\2\2\2N\u01d4\3\2\2\2P\u01d6\3")
        buf.write("\2\2\2R\u01dc\3\2\2\2T\u01e5\3\2\2\2V\u01ec\3\2\2\2X\u01ee")
        buf.write("\3\2\2\2Z\u01f9\3\2\2\2\\\u0204\3\2\2\2^\u0212\3\2\2\2")
        buf.write("`\u0217\3\2\2\2b\u0219\3\2\2\2d\u0223\3\2\2\2f\u0233\3")
        buf.write("\2\2\2h\u0238\3\2\2\2j\u0247\3\2\2\2l\u025d\3\2\2\2n\u025f")
        buf.write("\3\2\2\2pr\5\4\3\2qp\3\2\2\2rs\3\2\2\2sq\3\2\2\2st\3\2")
        buf.write("\2\2tu\3\2\2\2uv\7\2\2\3v\3\3\2\2\2wx\7\37\2\2x{\5P)\2")
        buf.write("yz\7C\2\2z|\5P)\2{y\3\2\2\2{|\3\2\2\2|}\3\2\2\2}\u0081")
        buf.write("\7=\2\2~\u0080\5\6\4\2\177~\3\2\2\2\u0080\u0083\3\2\2")
        buf.write("\2\u0081\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082\u0085\3")
        buf.write("\2\2\2\u0083\u0081\3\2\2\2\u0084\u0086\5\30\r\2\u0085")
        buf.write("\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u008a\3\2\2\2")
        buf.write("\u0087\u0089\5\6\4\2\u0088\u0087\3\2\2\2\u0089\u008c\3")
        buf.write("\2\2\2\u008a\u0088\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008d")
        buf.write("\3\2\2\2\u008c\u008a\3\2\2\2\u008d\u008e\7>\2\2\u008e")
        buf.write("\5\3\2\2\2\u008f\u0093\5\b\5\2\u0090\u0093\5\20\t\2\u0091")
        buf.write("\u0093\5\26\f\2\u0092\u008f\3\2\2\2\u0092\u0090\3\2\2")
        buf.write("\2\u0092\u0091\3\2\2\2\u0093\7\3\2\2\2\u0094\u0097\5\n")
        buf.write("\6\2\u0095\u0097\5\f\7\2\u0096\u0094\3\2\2\2\u0096\u0095")
        buf.write("\3\2\2\2\u0097\t\3\2\2\2\u0098\u0099\t\2\2\2\u0099\u009e")
        buf.write("\5P)\2\u009a\u009b\7A\2\2\u009b\u009d\5P)\2\u009c\u009a")
        buf.write("\3\2\2\2\u009d\u00a0\3\2\2\2\u009e\u009c\3\2\2\2\u009e")
        buf.write("\u009f\3\2\2\2\u009f\u00a1\3\2\2\2\u00a0\u009e\3\2\2\2")
        buf.write("\u00a1\u00a2\7C\2\2\u00a2\u00a3\5D#\2\u00a3\u00a4\7B\2")
        buf.write("\2\u00a4\13\3\2\2\2\u00a5\u00a6\t\2\2\2\u00a6\u00a7\5")
        buf.write("\16\b\2\u00a7\u00a8\7B\2\2\u00a8\r\3\2\2\2\u00a9\u00aa")
        buf.write("\5P)\2\u00aa\u00ab\7C\2\2\u00ab\u00ac\5D#\2\u00ac\u00ad")
        buf.write("\7\60\2\2\u00ad\u00ae\5T+\2\u00ae\u00b6\3\2\2\2\u00af")
        buf.write("\u00b0\5P)\2\u00b0\u00b1\7A\2\2\u00b1\u00b2\5\16\b\2\u00b2")
        buf.write("\u00b3\7A\2\2\u00b3\u00b4\5T+\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00a9\3\2\2\2\u00b5\u00af\3\2\2\2\u00b6\17\3\2\2\2\u00b7")
        buf.write("\u00b8\5P)\2\u00b8\u00ba\79\2\2\u00b9\u00bb\5\22\n\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\3\2\2\2")
        buf.write("\u00bc\u00bd\7:\2\2\u00bd\u00be\5\32\16\2\u00be\21\3\2")
        buf.write("\2\2\u00bf\u00c4\5\24\13\2\u00c0\u00c1\7B\2\2\u00c1\u00c3")
        buf.write("\5\24\13\2\u00c2\u00c0\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\23\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00cc\5P)\2\u00c8\u00c9\7A\2\2\u00c9")
        buf.write("\u00cb\5P)\2\u00ca\u00c8\3\2\2\2\u00cb\u00ce\3\2\2\2\u00cc")
        buf.write("\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cf\3\2\2\2")
        buf.write("\u00ce\u00cc\3\2\2\2\u00cf\u00d0\7C\2\2\u00d0\u00d1\5")
        buf.write("D#\2\u00d1\25\3\2\2\2\u00d2\u00d3\7\"\2\2\u00d3\u00d5")
        buf.write("\79\2\2\u00d4\u00d6\5\22\n\2\u00d5\u00d4\3\2\2\2\u00d5")
        buf.write("\u00d6\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d8\7:\2\2")
        buf.write("\u00d8\u00d9\5\32\16\2\u00d9\27\3\2\2\2\u00da\u00db\7")
        buf.write("#\2\2\u00db\u00dc\79\2\2\u00dc\u00dd\7:\2\2\u00dd\u00de")
        buf.write("\5\32\16\2\u00de\31\3\2\2\2\u00df\u00e3\7=\2\2\u00e0\u00e2")
        buf.write("\5\34\17\2\u00e1\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e6\3\2\2\2")
        buf.write("\u00e5\u00e3\3\2\2\2\u00e6\u00e7\7>\2\2\u00e7\33\3\2\2")
        buf.write("\2\u00e8\u00f1\5\36\20\2\u00e9\u00f1\5 \21\2\u00ea\u00f1")
        buf.write("\5\"\22\2\u00eb\u00f1\5$\23\2\u00ec\u00f1\5&\24\2\u00ed")
        buf.write("\u00f1\5(\25\2\u00ee\u00f1\5*\26\2\u00ef\u00f1\5\60\31")
        buf.write("\2\u00f0\u00e8\3\2\2\2\u00f0\u00e9\3\2\2\2\u00f0\u00ea")
        buf.write("\3\2\2\2\u00f0\u00eb\3\2\2\2\u00f0\u00ec\3\2\2\2\u00f0")
        buf.write("\u00ed\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2")
        buf.write("\u00f1\35\3\2\2\2\u00f2\u00f5\5> \2\u00f3\u00f5\5@!\2")
        buf.write("\u00f4\u00f2\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\37\3\2")
        buf.write("\2\2\u00f6\u00f9\5T+\2\u00f7\u00f8\7\60\2\2\u00f8\u00fa")
        buf.write("\5T+\2\u00f9\u00f7\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00f9")
        buf.write("\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd")
        buf.write("\u00fe\7B\2\2\u00fe!\3\2\2\2\u00ff\u0100\7\26\2\2\u0100")
        buf.write("\u0101\79\2\2\u0101\u0102\5T+\2\u0102\u0103\7:\2\2\u0103")
        buf.write("\u010c\5\32\16\2\u0104\u0105\7\27\2\2\u0105\u0106\79\2")
        buf.write("\2\u0106\u0107\5T+\2\u0107\u0108\7:\2\2\u0108\u0109\5")
        buf.write("\32\16\2\u0109\u010b\3\2\2\2\u010a\u0104\3\2\2\2\u010b")
        buf.write("\u010e\3\2\2\2\u010c\u010a\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u0111\3\2\2\2\u010e\u010c\3\2\2\2\u010f\u0110\7")
        buf.write("\30\2\2\u0110\u0112\5\32\16\2\u0111\u010f\3\2\2\2\u0111")
        buf.write("\u0112\3\2\2\2\u0112#\3\2\2\2\u0113\u0114\7\31\2\2\u0114")
        buf.write("\u0115\79\2\2\u0115\u0116\7D\2\2\u0116\u0117\7\35\2\2")
        buf.write("\u0117\u0118\5T+\2\u0118\u0119\7@\2\2\u0119\u011c\5T+")
        buf.write("\2\u011a\u011b\7%\2\2\u011b\u011d\5T+\2\u011c\u011a\3")
        buf.write("\2\2\2\u011c\u011d\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f")
        buf.write("\7:\2\2\u011f\u0120\5\32\16\2\u0120%\3\2\2\2\u0121\u0122")
        buf.write("\7\24\2\2\u0122\u0123\7B\2\2\u0123\'\3\2\2\2\u0124\u0125")
        buf.write("\7\25\2\2\u0125\u0126\7B\2\2\u0126)\3\2\2\2\u0127\u0129")
        buf.write("\7\23\2\2\u0128\u012a\5T+\2\u0129\u0128\3\2\2\2\u0129")
        buf.write("\u012a\3\2\2\2\u012a\u012b\3\2\2\2\u012b\u012c\7B\2\2")
        buf.write("\u012c+\3\2\2\2\u012d\u012e\5b\62\2\u012e\u012f\7?\2\2")
        buf.write("\u012f\u0130\7D\2\2\u0130\u0139\79\2\2\u0131\u0136\5T")
        buf.write("+\2\u0132\u0133\7A\2\2\u0133\u0135\5T+\2\u0134\u0132\3")
        buf.write("\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137")
        buf.write("\3\2\2\2\u0137\u013a\3\2\2\2\u0138\u0136\3\2\2\2\u0139")
        buf.write("\u0131\3\2\2\2\u0139\u013a\3\2\2\2\u013a\u013b\3\2\2\2")
        buf.write("\u013b\u013c\7:\2\2\u013c\u013d\7B\2\2\u013d-\3\2\2\2")
        buf.write("\u013e\u013f\5d\63\2\u013f\u0140\78\2\2\u0140\u0141\7")
        buf.write("E\2\2\u0141\u014a\79\2\2\u0142\u0147\5T+\2\u0143\u0144")
        buf.write("\7A\2\2\u0144\u0146\5T+\2\u0145\u0143\3\2\2\2\u0146\u0149")
        buf.write("\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0148\3\2\2\2\u0148")
        buf.write("\u014b\3\2\2\2\u0149\u0147\3\2\2\2\u014a\u0142\3\2\2\2")
        buf.write("\u014a\u014b\3\2\2\2\u014b\u014c\3\2\2\2\u014c\u014d\7")
        buf.write(":\2\2\u014d\u014e\7B\2\2\u014e/\3\2\2\2\u014f\u0152\5")
        buf.write("\64\33\2\u0150\u0152\5\66\34\2\u0151\u014f\3\2\2\2\u0151")
        buf.write("\u0150\3\2\2\2\u0152\61\3\2\2\2\u0153\u0156\5\64\33\2")
        buf.write("\u0154\u0156\5\66\34\2\u0155\u0153\3\2\2\2\u0155\u0154")
        buf.write("\3\2\2\2\u0156\63\3\2\2\2\u0157\u015a\5P)\2\u0158\u015a")
        buf.write("\7&\2\2\u0159\u0157\3\2\2\2\u0159\u0158\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\u015c\7?\2\2\u015c\u015d\7D\2\2\u015d")
        buf.write("\u0166\79\2\2\u015e\u0163\5T+\2\u015f\u0160\7A\2\2\u0160")
        buf.write("\u0162\5T+\2\u0161\u015f\3\2\2\2\u0162\u0165\3\2\2\2\u0163")
        buf.write("\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0167\3\2\2\2")
        buf.write("\u0165\u0163\3\2\2\2\u0166\u015e\3\2\2\2\u0166\u0167\3")
        buf.write("\2\2\2\u0167\u0168\3\2\2\2\u0168\u016a\7:\2\2\u0169\u016b")
        buf.write("\7B\2\2\u016a\u0169\3\2\2\2\u016a\u016b\3\2\2\2\u016b")
        buf.write("\65\3\2\2\2\u016c\u016f\5P)\2\u016d\u016f\7&\2\2\u016e")
        buf.write("\u016c\3\2\2\2\u016e\u016d\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0171\78\2\2\u0171\u0172\7E\2\2\u0172\u017b\79")
        buf.write("\2\2\u0173\u0178\5T+\2\u0174\u0175\7A\2\2\u0175\u0177")
        buf.write("\5T+\2\u0176\u0174\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0179\3\2\2\2\u0179\u017c\3\2\2\2\u017a")
        buf.write("\u0178\3\2\2\2\u017b\u0173\3\2\2\2\u017b\u017c\3\2\2\2")
        buf.write("\u017c\u017d\3\2\2\2\u017d\u017f\7:\2\2\u017e\u0180\7")
        buf.write("B\2\2\u017f\u017e\3\2\2\2\u017f\u0180\3\2\2\2\u0180\67")
        buf.write("\3\2\2\2\u0181\u0184\5:\36\2\u0182\u0184\5<\37\2\u0183")
        buf.write("\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u01849\3\2\2\2\u0185")
        buf.write("\u0186\5T+\2\u0186\u0187\7?\2\2\u0187\u0188\7D\2\2\u0188")
        buf.write(";\3\2\2\2\u0189\u018e\5P)\2\u018a\u018e\7&\2\2\u018b\u018c")
        buf.write("\t\3\2\2\u018c\u018e\5R*\2\u018d\u0189\3\2\2\2\u018d\u018a")
        buf.write("\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u018f\3\2\2\2\u018f")
        buf.write("\u0190\78\2\2\u0190\u0191\7E\2\2\u0191=\3\2\2\2\u0192")
        buf.write("\u0193\t\2\2\2\u0193\u0198\7D\2\2\u0194\u0195\7A\2\2\u0195")
        buf.write("\u0197\7D\2\2\u0196\u0194\3\2\2\2\u0197\u019a\3\2\2\2")
        buf.write("\u0198\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019b\3")
        buf.write("\2\2\2\u019a\u0198\3\2\2\2\u019b\u019c\7C\2\2\u019c\u019d")
        buf.write("\5D#\2\u019d\u019e\7B\2\2\u019e?\3\2\2\2\u019f\u01a0\t")
        buf.write("\2\2\2\u01a0\u01a1\5B\"\2\u01a1\u01a2\7B\2\2\u01a2A\3")
        buf.write("\2\2\2\u01a3\u01a4\7D\2\2\u01a4\u01a5\7C\2\2\u01a5\u01a6")
        buf.write("\5D#\2\u01a6\u01a7\7\60\2\2\u01a7\u01a8\5T+\2\u01a8\u01b0")
        buf.write("\3\2\2\2\u01a9\u01aa\7D\2\2\u01aa\u01ab\7A\2\2\u01ab\u01ac")
        buf.write("\5B\"\2\u01ac\u01ad\7A\2\2\u01ad\u01ae\5T+\2\u01ae\u01b0")
        buf.write("\3\2\2\2\u01af\u01a3\3\2\2\2\u01af\u01a9\3\2\2\2\u01b0")
        buf.write("C\3\2\2\2\u01b1\u01b5\5F$\2\u01b2\u01b5\5H%\2\u01b3\u01b5")
        buf.write("\5J&\2\u01b4\u01b1\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3")
        buf.write("\3\2\2\2\u01b5E\3\2\2\2\u01b6\u01b7\t\4\2\2\u01b7G\3\2")
        buf.write("\2\2\u01b8\u01b9\7\34\2\2\u01b9\u01bd\7;\2\2\u01ba\u01be")
        buf.write("\5F$\2\u01bb\u01be\5H%\2\u01bc\u01be\5J&\2\u01bd\u01ba")
        buf.write("\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bf\u01c0\7A\2\2\u01c0\u01c1\7\4\2\2")
        buf.write("\u01c1\u01c2\7<\2\2\u01c2I\3\2\2\2\u01c3\u01c4\7D\2\2")
        buf.write("\u01c4K\3\2\2\2\u01c5\u01c6\7$\2\2\u01c6\u01c7\7D\2\2")
        buf.write("\u01c7\u01d0\79\2\2\u01c8\u01cd\5T+\2\u01c9\u01ca\7A\2")
        buf.write("\2\u01ca\u01cc\5T+\2\u01cb\u01c9\3\2\2\2\u01cc\u01cf\3")
        buf.write("\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d1")
        buf.write("\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01c8\3\2\2\2\u01d0")
        buf.write("\u01d1\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\7:\2\2")
        buf.write("\u01d3M\3\2\2\2\u01d4\u01d5\t\5\2\2\u01d5O\3\2\2\2\u01d6")
        buf.write("\u01d7\t\3\2\2\u01d7Q\3\2\2\2\u01d8\u01d9\7;\2\2\u01d9")
        buf.write("\u01da\5T+\2\u01da\u01db\7<\2\2\u01db\u01dd\3\2\2\2\u01dc")
        buf.write("\u01d8\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01dc\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01dfS\3\2\2\2\u01e0\u01e1\5V,\2")
        buf.write("\u01e1\u01e2\t\6\2\2\u01e2\u01e3\5V,\2\u01e3\u01e6\3\2")
        buf.write("\2\2\u01e4\u01e6\5V,\2\u01e5\u01e0\3\2\2\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6U\3\2\2\2\u01e7\u01e8\5X-\2\u01e8\u01e9")
        buf.write("\t\7\2\2\u01e9\u01ea\5X-\2\u01ea\u01ed\3\2\2\2\u01eb\u01ed")
        buf.write("\5X-\2\u01ec\u01e7\3\2\2\2\u01ec\u01eb\3\2\2\2\u01edW")
        buf.write("\3\2\2\2\u01ee\u01ef\b-\1\2\u01ef\u01f0\5Z.\2\u01f0\u01f6")
        buf.write("\3\2\2\2\u01f1\u01f2\f\4\2\2\u01f2\u01f3\t\b\2\2\u01f3")
        buf.write("\u01f5\5Z.\2\u01f4\u01f1\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7Y\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f9\u01fa\b.\1\2\u01fa\u01fb\5\\/\2\u01fb")
        buf.write("\u0201\3\2\2\2\u01fc\u01fd\f\4\2\2\u01fd\u01fe\t\t\2\2")
        buf.write("\u01fe\u0200\5\\/\2\u01ff\u01fc\3\2\2\2\u0200\u0203\3")
        buf.write("\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202[")
        buf.write("\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205\b/\1\2\u0205")
        buf.write("\u0206\5^\60\2\u0206\u020c\3\2\2\2\u0207\u0208\f\4\2\2")
        buf.write("\u0208\u0209\t\n\2\2\u0209\u020b\5^\60\2\u020a\u0207\3")
        buf.write("\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c\u020d")
        buf.write("\3\2\2\2\u020d]\3\2\2\2\u020e\u020c\3\2\2\2\u020f\u0210")
        buf.write("\7,\2\2\u0210\u0213\5^\60\2\u0211\u0213\5`\61\2\u0212")
        buf.write("\u020f\3\2\2\2\u0212\u0211\3\2\2\2\u0213_\3\2\2\2\u0214")
        buf.write("\u0215\7(\2\2\u0215\u0218\5`\61\2\u0216\u0218\5b\62\2")
        buf.write("\u0217\u0214\3\2\2\2\u0217\u0216\3\2\2\2\u0218a\3\2\2")
        buf.write("\2\u0219\u021a\b\62\1\2\u021a\u021b\5d\63\2\u021b\u0220")
        buf.write("\3\2\2\2\u021c\u021d\f\4\2\2\u021d\u021f\5R*\2\u021e\u021c")
        buf.write("\3\2\2\2\u021f\u0222\3\2\2\2\u0220\u021e\3\2\2\2\u0220")
        buf.write("\u0221\3\2\2\2\u0221c\3\2\2\2\u0222\u0220\3\2\2\2\u0223")
        buf.write("\u0224\b\63\1\2\u0224\u0225\5f\64\2\u0225\u022b\3\2\2")
        buf.write("\2\u0226\u0227\f\4\2\2\u0227\u0228\7?\2\2\u0228\u022a")
        buf.write("\5f\64\2\u0229\u0226\3\2\2\2\u022a\u022d\3\2\2\2\u022b")
        buf.write("\u0229\3\2\2\2\u022b\u022c\3\2\2\2\u022ce\3\2\2\2\u022d")
        buf.write("\u022b\3\2\2\2\u022e\u022f\5h\65\2\u022f\u0230\78\2\2")
        buf.write("\u0230\u0231\5h\65\2\u0231\u0234\3\2\2\2\u0232\u0234\5")
        buf.write("h\65\2\u0233\u022e\3\2\2\2\u0233\u0232\3\2\2\2\u0234g")
        buf.write("\3\2\2\2\u0235\u0236\7$\2\2\u0236\u0239\5h\65\2\u0237")
        buf.write("\u0239\5j\66\2\u0238\u0235\3\2\2\2\u0238\u0237\3\2\2\2")
        buf.write("\u0239i\3\2\2\2\u023a\u0248\5N(\2\u023b\u0248\5\62\32")
        buf.write("\2\u023c\u0248\7&\2\2\u023d\u023e\t\3\2\2\u023e\u0248")
        buf.write("\5R*\2\u023f\u0248\5n8\2\u0240\u0248\7\36\2\2\u0241\u0248")
        buf.write("\5L\'\2\u0242\u0248\5P)\2\u0243\u0244\79\2\2\u0244\u0245")
        buf.write("\5T+\2\u0245\u0246\7:\2\2\u0246\u0248\3\2\2\2\u0247\u023a")
        buf.write("\3\2\2\2\u0247\u023b\3\2\2\2\u0247\u023c\3\2\2\2\u0247")
        buf.write("\u023d\3\2\2\2\u0247\u023f\3\2\2\2\u0247\u0240\3\2\2\2")
        buf.write("\u0247\u0241\3\2\2\2\u0247\u0242\3\2\2\2\u0247\u0243\3")
        buf.write("\2\2\2\u0248k\3\2\2\2\u0249\u024e\5n8\2\u024a\u024b\7")
        buf.write("A\2\2\u024b\u024d\5n8\2\u024c\u024a\3\2\2\2\u024d\u0250")
        buf.write("\3\2\2\2\u024e\u024c\3\2\2\2\u024e\u024f\3\2\2\2\u024f")
        buf.write("\u025e\3\2\2\2\u0250\u024e\3\2\2\2\u0251\u0252\7\34\2")
        buf.write("\2\u0252\u0253\79\2\2\u0253\u0258\5l\67\2\u0254\u0255")
        buf.write("\7A\2\2\u0255\u0257\5l\67\2\u0256\u0254\3\2\2\2\u0257")
        buf.write("\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259\3\2\2\2")
        buf.write("\u0259\u025b\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c\7")
        buf.write(":\2\2\u025c\u025e\3\2\2\2\u025d\u0249\3\2\2\2\u025d\u0251")
        buf.write("\3\2\2\2\u025em\3\2\2\2\u025f\u0260\7\34\2\2\u0260\u0261")
        buf.write("\79\2\2\u0261\u0266\5T+\2\u0262\u0263\7A\2\2\u0263\u0265")
        buf.write("\5T+\2\u0264\u0262\3\2\2\2\u0265\u0268\3\2\2\2\u0266\u0264")
        buf.write("\3\2\2\2\u0266\u0267\3\2\2\2\u0267\u0269\3\2\2\2\u0268")
        buf.write("\u0266\3\2\2\2\u0269\u026a\7:\2\2\u026ao\3\2\2\2>s{\u0081")
        buf.write("\u0085\u008a\u0092\u0096\u009e\u00b5\u00ba\u00c4\u00cc")
        buf.write("\u00d5\u00e3\u00f0\u00f4\u00fb\u010c\u0111\u011c\u0129")
        buf.write("\u0136\u0139\u0147\u014a\u0151\u0155\u0159\u0163\u0166")
        buf.write("\u016a\u016e\u0178\u017b\u017f\u0183\u018d\u0198\u01af")
        buf.write("\u01b4\u01bd\u01cd\u01d0\u01de\u01e5\u01ec\u01f6\u0201")
        buf.write("\u020c\u0212\u0217\u0220\u022b\u0233\u0238\u0247\u024e")
        buf.write("\u0258\u025d\u0266")
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
    RULE_instance_call = 21
    RULE_static_call = 22
    RULE_method_invocate_statement = 23
    RULE_method_invocate_expression = 24
    RULE_instance_method_invocate = 25
    RULE_static_method_invocate = 26
    RULE_attribute_access = 27
    RULE_instance_attribute_access = 28
    RULE_static_attribute_access = 29
    RULE_var_const_decl_1 = 30
    RULE_var_const_decl_2 = 31
    RULE_var_const_testing = 32
    RULE_data_types = 33
    RULE_primitive_types = 34
    RULE_array_type = 35
    RULE_class_type = 36
    RULE_class_new_object = 37
    RULE_literals = 38
    RULE_identifier = 39
    RULE_index_id = 40
    RULE_expr = 41
    RULE_expr_1 = 42
    RULE_expr_2 = 43
    RULE_expr_3 = 44
    RULE_expr_4 = 45
    RULE_expr_5 = 46
    RULE_expr_6 = 47
    RULE_expr_7 = 48
    RULE_expr_8 = 49
    RULE_expr_9 = 50
    RULE_expr_10 = 51
    RULE_expr_11 = 52
    RULE_multi_dimensional_arrays = 53
    RULE_indexed_array = 54

    ruleNames =  [ "program", "class_decl", "member_list", "attribute_decl", 
                   "attribute_decl_1", "attribute_decl_2", "attribute_testing", 
                   "method_decl", "parameter_list", "parameter", "constructor", 
                   "destructor", "block_statement", "statement", "var_const_decl_statement", 
                   "assign_statement", "if_statement", "for_statement", 
                   "break_statement", "continue_statement", "return_statement", 
                   "instance_call", "static_call", "method_invocate_statement", 
                   "method_invocate_expression", "instance_method_invocate", 
                   "static_method_invocate", "attribute_access", "instance_attribute_access", 
                   "static_attribute_access", "var_const_decl_1", "var_const_decl_2", 
                   "var_const_testing", "data_types", "primitive_types", 
                   "array_type", "class_type", "class_new_object", "literals", 
                   "identifier", "index_id", "expr", "expr_1", "expr_2", 
                   "expr_3", "expr_4", "expr_5", "expr_6", "expr_7", "expr_8", 
                   "expr_9", "expr_10", "expr_11", "multi_dimensional_arrays", 
                   "indexed_array" ]

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
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 110
                self.class_decl()
                self.state = 113 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 115
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_decl" ):
                return visitor.visitClass_decl(self)
            else:
                return visitor.visitChildren(self)




    def class_decl(self):

        localctx = D96Parser.Class_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(D96Parser.CLASS)
            self.state = 118
            self.identifier()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 119
                self.match(D96Parser.COLON)
                self.state = 120
                self.identifier()


            self.state = 123
            self.match(D96Parser.LCB)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 124
                    self.member_list() 
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.DESTRUCTOR:
                self.state = 130
                self.destructor()


            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & ((1 << (D96Parser.VAL - 30)) | (1 << (D96Parser.VAR - 30)) | (1 << (D96Parser.CONSTRUCTOR - 30)) | (1 << (D96Parser.ID - 30)) | (1 << (D96Parser.DOLLAR_ID - 30)))) != 0):
                self.state = 133
                self.member_list()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_list" ):
                return visitor.visitMember_list(self)
            else:
                return visitor.visitChildren(self)




    def member_list(self):

        localctx = D96Parser.Member_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_member_list)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.attribute_decl()
                pass
            elif token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.method_decl()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 143
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attribute_decl_1(self):
            return self.getTypedRuleContext(D96Parser.Attribute_decl_1Context,0)


        def attribute_decl_2(self):
            return self.getTypedRuleContext(D96Parser.Attribute_decl_2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl" ):
                return visitor.visitAttribute_decl(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl(self):

        localctx = D96Parser.Attribute_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attribute_decl)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.attribute_decl_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl_1" ):
                return visitor.visitAttribute_decl_1(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl_1(self):

        localctx = D96Parser.Attribute_decl_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attribute_decl_1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 151
            self.identifier()
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 152
                self.match(D96Parser.COMMA)
                self.state = 153
                self.identifier()
                self.state = 158
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 159
            self.match(D96Parser.COLON)
            self.state = 160
            self.data_types()
            self.state = 161
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_decl_2Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_decl_2" ):
                return visitor.visitAttribute_decl_2(self)
            else:
                return visitor.visitChildren(self)




    def attribute_decl_2(self):

        localctx = D96Parser.Attribute_decl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_attribute_decl_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 164
            self.attribute_testing()
            self.state = 165
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_testingContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_testing" ):
                return visitor.visitAttribute_testing(self)
            else:
                return visitor.visitChildren(self)




    def attribute_testing(self):

        localctx = D96Parser.Attribute_testingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_attribute_testing)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.identifier()
                self.state = 168
                self.match(D96Parser.COLON)
                self.state = 169
                self.data_types()
                self.state = 170
                self.match(D96Parser.ASSIGN)
                self.state = 171
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.identifier()
                self.state = 174
                self.match(D96Parser.COMMA)
                self.state = 175
                self.attribute_testing()

                self.state = 176
                self.match(D96Parser.COMMA)
                self.state = 177
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_decl" ):
                return visitor.visitMethod_decl(self)
            else:
                return visitor.visitChildren(self)




    def method_decl(self):

        localctx = D96Parser.Method_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_method_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.identifier()
            self.state = 182
            self.match(D96Parser.LP)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 183
                self.parameter_list()


            self.state = 186
            self.match(D96Parser.RP)
            self.state = 187
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_list" ):
                return visitor.visitParameter_list(self)
            else:
                return visitor.visitChildren(self)




    def parameter_list(self):

        localctx = D96Parser.Parameter_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_parameter_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.parameter()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SEMI:
                self.state = 190
                self.match(D96Parser.SEMI)
                self.state = 191
                self.parameter()
                self.state = 196
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = D96Parser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.identifier()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 198
                self.match(D96Parser.COMMA)
                self.state = 199
                self.identifier()
                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 205
            self.match(D96Parser.COLON)
            self.state = 206
            self.data_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor" ):
                return visitor.visitConstructor(self)
            else:
                return visitor.visitChildren(self)




    def constructor(self):

        localctx = D96Parser.ConstructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constructor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 209
            self.match(D96Parser.LP)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 210
                self.parameter_list()


            self.state = 213
            self.match(D96Parser.RP)
            self.state = 214
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestructorContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor" ):
                return visitor.visitDestructor(self)
            else:
                return visitor.visitChildren(self)




    def destructor(self):

        localctx = D96Parser.DestructorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_destructor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(D96Parser.DESTRUCTOR)
            self.state = 217
            self.match(D96Parser.LP)
            self.state = 218
            self.match(D96Parser.RP)
            self.state = 219
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = D96Parser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(D96Parser.LCB)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.RETURN) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 222
                self.statement()
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 228
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.var_const_decl_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.assign_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 232
                self.if_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 233
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 234
                self.break_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 235
                self.continue_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 236
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 237
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_const_decl_1(self):
            return self.getTypedRuleContext(D96Parser.Var_const_decl_1Context,0)


        def var_const_decl_2(self):
            return self.getTypedRuleContext(D96Parser.Var_const_decl_2Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_const_decl_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_const_decl_statement" ):
                return visitor.visitVar_const_decl_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_const_decl_statement(self):

        localctx = D96Parser.Var_const_decl_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_const_decl_statement)
        try:
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.var_const_decl_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_statement" ):
                return visitor.visitAssign_statement(self)
            else:
                return visitor.visitChildren(self)




    def assign_statement(self):

        localctx = D96Parser.Assign_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.expr()
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 245
                self.match(D96Parser.ASSIGN)
                self.state = 246
                self.expr()
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.ASSIGN):
                    break

            self.state = 251
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = D96Parser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(D96Parser.IF)
            self.state = 254
            self.match(D96Parser.LP)
            self.state = 255
            self.expr()
            self.state = 256
            self.match(D96Parser.RP)
            self.state = 257
            self.block_statement()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 258
                self.match(D96Parser.ELSEIF)
                self.state = 259
                self.match(D96Parser.LP)
                self.state = 260
                self.expr()
                self.state = 261
                self.match(D96Parser.RP)
                self.state = 262
                self.block_statement()
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 269
                self.match(D96Parser.ELSE)
                self.state = 270
                self.block_statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = D96Parser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(D96Parser.FOREACH)
            self.state = 274
            self.match(D96Parser.LP)
            self.state = 275
            self.match(D96Parser.ID)
            self.state = 276
            self.match(D96Parser.IN)
            self.state = 277
            self.expr()
            self.state = 278
            self.match(D96Parser.DOUBLEDOT)
            self.state = 279
            self.expr()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 280
                self.match(D96Parser.BY)
                self.state = 281
                self.expr()


            self.state = 284
            self.match(D96Parser.RP)
            self.state = 285
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = D96Parser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(D96Parser.BREAK)
            self.state = 288
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = D96Parser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(D96Parser.CONTINUE)
            self.state = 291
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = D96Parser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(D96Parser.RETURN)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 294
                self.expr()


            self.state = 297
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_callContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr_7(self):
            return self.getTypedRuleContext(D96Parser.Expr_7Context,0)


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
            return D96Parser.RULE_instance_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_call" ):
                return visitor.visitInstance_call(self)
            else:
                return visitor.visitChildren(self)




    def instance_call(self):

        localctx = D96Parser.Instance_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_instance_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.expr_7(0)
            self.state = 300
            self.match(D96Parser.DOT)
            self.state = 301
            self.match(D96Parser.ID)
            self.state = 302
            self.match(D96Parser.LP)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 303
                self.expr()
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 304
                    self.match(D96Parser.COMMA)
                    self.state = 305
                    self.expr()
                    self.state = 310
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 313
            self.match(D96Parser.RP)
            self.state = 314
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_callContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def SEMI(self):
            return self.getToken(D96Parser.SEMI, 0)

        def expr_8(self):
            return self.getTypedRuleContext(D96Parser.Expr_8Context,0)


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
            return D96Parser.RULE_static_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_call" ):
                return visitor.visitStatic_call(self)
            else:
                return visitor.visitChildren(self)




    def static_call(self):

        localctx = D96Parser.Static_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_static_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.expr_8(0)
            self.state = 317
            self.match(D96Parser.STATIC_GLOBAL_DOT)
            self.state = 318
            self.match(D96Parser.DOLLAR_ID)
            self.state = 319
            self.match(D96Parser.LP)
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 320
                self.expr()
                self.state = 325
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 321
                    self.match(D96Parser.COMMA)
                    self.state = 322
                    self.expr()
                    self.state = 327
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 330
            self.match(D96Parser.RP)
            self.state = 331
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocate_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invocateContext,0)


        def static_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocateContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocate_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocate_statement" ):
                return visitor.visitMethod_invocate_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocate_statement(self):

        localctx = D96Parser.Method_invocate_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_method_invocate_statement)
        try:
            self.state = 335
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.instance_method_invocate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_invocateContext,0)


        def static_method_invocate(self):
            return self.getTypedRuleContext(D96Parser.Static_method_invocateContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocate_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocate_expression" ):
                return visitor.visitMethod_invocate_expression(self)
            else:
                return visitor.visitChildren(self)




    def method_invocate_expression(self):

        localctx = D96Parser.Method_invocate_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_method_invocate_expression)
        try:
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.instance_method_invocate()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_invocate" ):
                return visitor.visitInstance_method_invocate(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_invocate(self):

        localctx = D96Parser.Instance_method_invocateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_instance_method_invocate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.state = 341
                self.identifier()
                pass
            elif token in [D96Parser.SELF]:
                self.state = 342
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 345
            self.match(D96Parser.DOT)
            self.state = 346
            self.match(D96Parser.ID)
            self.state = 347
            self.match(D96Parser.LP)
            self.state = 356
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 348
                self.expr()
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 349
                    self.match(D96Parser.COMMA)
                    self.state = 350
                    self.expr()
                    self.state = 355
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 358
            self.match(D96Parser.RP)
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 359
                self.match(D96Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_invocateContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_invocate" ):
                return visitor.visitStatic_method_invocate(self)
            else:
                return visitor.visitChildren(self)




    def static_method_invocate(self):

        localctx = D96Parser.Static_method_invocateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_static_method_invocate)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.state = 362
                self.identifier()
                pass
            elif token in [D96Parser.SELF]:
                self.state = 363
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 366
            self.match(D96Parser.STATIC_GLOBAL_DOT)
            self.state = 367
            self.match(D96Parser.DOLLAR_ID)
            self.state = 368
            self.match(D96Parser.LP)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 369
                self.expr()
                self.state = 374
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 370
                    self.match(D96Parser.COMMA)
                    self.state = 371
                    self.expr()
                    self.state = 376
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 379
            self.match(D96Parser.RP)
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 380
                self.match(D96Parser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attribute_accessContext,0)


        def static_attribute_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attribute_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttribute_access" ):
                return visitor.visitAttribute_access(self)
            else:
                return visitor.visitChildren(self)




    def attribute_access(self):

        localctx = D96Parser.Attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_attribute_access)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.instance_attribute_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attribute_access" ):
                return visitor.visitInstance_attribute_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_attribute_access(self):

        localctx = D96Parser.Instance_attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_instance_attribute_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.expr()
            self.state = 388
            self.match(D96Parser.DOT)
            self.state = 389
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attribute_accessContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attribute_access" ):
                return visitor.visitStatic_attribute_access(self)
            else:
                return visitor.visitChildren(self)




    def static_attribute_access(self):

        localctx = D96Parser.Static_attribute_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_static_attribute_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 391
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 392
                self.match(D96Parser.SELF)
                pass

            elif la_ == 3:
                self.state = 393
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 394
                self.index_id()
                pass


            self.state = 397
            self.match(D96Parser.STATIC_GLOBAL_DOT)
            self.state = 398
            self.match(D96Parser.DOLLAR_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_decl_1Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_const_decl_1" ):
                return visitor.visitVar_const_decl_1(self)
            else:
                return visitor.visitChildren(self)




    def var_const_decl_1(self):

        localctx = D96Parser.Var_const_decl_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_var_const_decl_1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 401
            self.match(D96Parser.ID)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 402
                self.match(D96Parser.COMMA)
                self.state = 403
                self.match(D96Parser.ID)
                self.state = 408
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 409
            self.match(D96Parser.COLON)
            self.state = 410
            self.data_types()
            self.state = 411
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_decl_2Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_const_decl_2" ):
                return visitor.visitVar_const_decl_2(self)
            else:
                return visitor.visitChildren(self)




    def var_const_decl_2(self):

        localctx = D96Parser.Var_const_decl_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_var_const_decl_2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 414
            self.var_const_testing()
            self.state = 415
            self.match(D96Parser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_const_testingContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_const_testing" ):
                return visitor.visitVar_const_testing(self)
            else:
                return visitor.visitChildren(self)




    def var_const_testing(self):

        localctx = D96Parser.Var_const_testingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_var_const_testing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.state = 417
                self.match(D96Parser.ID)
                self.state = 418
                self.match(D96Parser.COLON)
                self.state = 419
                self.data_types()
                self.state = 420
                self.match(D96Parser.ASSIGN)
                self.state = 421
                self.expr()
                pass

            elif la_ == 2:
                self.state = 423
                self.match(D96Parser.ID)
                self.state = 424
                self.match(D96Parser.COMMA)
                self.state = 425
                self.var_const_testing()

                self.state = 426
                self.match(D96Parser.COMMA)
                self.state = 427
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_types" ):
                return visitor.visitData_types(self)
            else:
                return visitor.visitChildren(self)




    def data_types(self):

        localctx = D96Parser.Data_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_data_types)
        try:
            self.state = 434
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_TYPE, D96Parser.FLOAT_TYPE, D96Parser.STRING_TYPE, D96Parser.BOOLEAN_TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_types" ):
                return visitor.visitPrimitive_types(self)
            else:
                return visitor.visitChildren(self)




    def primitive_types(self):

        localctx = D96Parser.Primitive_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(D96Parser.ARRAY)
            self.state = 439
            self.match(D96Parser.LSB)
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT_TYPE, D96Parser.FLOAT_TYPE, D96Parser.STRING_TYPE, D96Parser.BOOLEAN_TYPE]:
                self.state = 440
                self.primitive_types()
                pass
            elif token in [D96Parser.ARRAY]:
                self.state = 441
                self.array_type()
                pass
            elif token in [D96Parser.ID]:
                self.state = 442
                self.class_type()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 445
            self.match(D96Parser.COMMA)
            self.state = 446
            self.match(D96Parser.NATURAL)
            self.state = 447
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_type" ):
                return visitor.visitClass_type(self)
            else:
                return visitor.visitChildren(self)




    def class_type(self):

        localctx = D96Parser.Class_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_class_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_new_objectContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_new_object" ):
                return visitor.visitClass_new_object(self)
            else:
                return visitor.visitChildren(self)




    def class_new_object(self):

        localctx = D96Parser.Class_new_objectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_class_new_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(D96Parser.NEW)
            self.state = 452
            self.match(D96Parser.ID)
            self.state = 453
            self.match(D96Parser.LP)
            self.state = 462
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLEAN_LITERAL) | (1 << D96Parser.NATURAL) | (1 << D96Parser.INTEGER_LIERAL) | (1 << D96Parser.FLOAT_LITERAL) | (1 << D96Parser.STRING_LITERAL) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NULL) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LP))) != 0) or _la==D96Parser.ID or _la==D96Parser.DOLLAR_ID:
                self.state = 454
                self.expr()
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 455
                    self.match(D96Parser.COMMA)
                    self.state = 456
                    self.expr()
                    self.state = 461
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 464
            self.match(D96Parser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiterals" ):
                return visitor.visitLiterals(self)
            else:
                return visitor.visitChildren(self)




    def literals(self):

        localctx = D96Parser.LiteralsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_literals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def DOLLAR_ID(self):
            return self.getToken(D96Parser.DOLLAR_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = D96Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_id" ):
                return visitor.visitIndex_id(self)
            else:
                return visitor.visitChildren(self)




    def index_id(self):

        localctx = D96Parser.Index_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_index_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 470
                    self.match(D96Parser.LSB)
                    self.state = 471
                    self.expr()
                    self.state = 472
                    self.match(D96Parser.RSB)

                else:
                    raise NoViableAltException(self)
                self.state = 476 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.expr_1()
                self.state = 479
                _la = self._input.LA(1)
                if not(_la==D96Parser.STRING_CONCATE or _la==D96Parser.STRING_COMPARE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 480
                self.expr_1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_1" ):
                return visitor.visitExpr_1(self)
            else:
                return visitor.visitChildren(self)




    def expr_1(self):

        localctx = D96Parser.Expr_1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr_1)
        self._la = 0 # Token type
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.expr_2(0)
                self.state = 486
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUAL) | (1 << D96Parser.NOT_EQUAL) | (1 << D96Parser.LESS_THAN) | (1 << D96Parser.LESS_THAN_EQUAL) | (1 << D96Parser.GREATER_THAN) | (1 << D96Parser.GREATER_THAN_EQUAL))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 487
                self.expr_2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_2" ):
                return visitor.visitExpr_2(self)
            else:
                return visitor.visitChildren(self)



    def expr_2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr_2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.expr_3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,46,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_2)
                    self.state = 495
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 496
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.AND or _la==D96Parser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 497
                    self.expr_3(0) 
                self.state = 502
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,46,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_3Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_3" ):
                return visitor.visitExpr_3(self)
            else:
                return visitor.visitChildren(self)



    def expr_3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr_3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.expr_4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_3)
                    self.state = 506
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 507
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 508
                    self.expr_4(0) 
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_4Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_4" ):
                return visitor.visitExpr_4(self)
            else:
                return visitor.visitChildren(self)



    def expr_4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr_4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.expr_5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 522
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_4)
                    self.state = 517
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 518
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 519
                    self.expr_5() 
                self.state = 524
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_5Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_5" ):
                return visitor.visitExpr_5(self)
            else:
                return visitor.visitChildren(self)




    def expr_5(self):

        localctx = D96Parser.Expr_5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr_5)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(D96Parser.NOT)
                self.state = 526
                self.expr_5()
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL, D96Parser.NATURAL, D96Parser.INTEGER_LIERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.SUB, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_6" ):
                return visitor.visitExpr_6(self)
            else:
                return visitor.visitChildren(self)




    def expr_6(self):

        localctx = D96Parser.Expr_6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr_6)
        try:
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(D96Parser.SUB)
                self.state = 531
                self.expr_6()
                pass
            elif token in [D96Parser.BOOLEAN_LITERAL, D96Parser.NATURAL, D96Parser.INTEGER_LIERAL, D96Parser.FLOAT_LITERAL, D96Parser.STRING_LITERAL, D96Parser.ARRAY, D96Parser.NULL, D96Parser.NEW, D96Parser.SELF, D96Parser.LP, D96Parser.ID, D96Parser.DOLLAR_ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_7" ):
                return visitor.visitExpr_7(self)
            else:
                return visitor.visitChildren(self)



    def expr_7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr_7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.expr_8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 542
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_7)
                    self.state = 538
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 539
                    self.index_id() 
                self.state = 544
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_8Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_8" ):
                return visitor.visitExpr_8(self)
            else:
                return visitor.visitChildren(self)



    def expr_8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr_8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 98
        self.enterRecursionRule(localctx, 98, self.RULE_expr_8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.expr_9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 553
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr_8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr_8)
                    self.state = 548
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 549
                    self.match(D96Parser.DOT)
                    self.state = 550
                    self.expr_9() 
                self.state = 555
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr_9Context(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_9" ):
                return visitor.visitExpr_9(self)
            else:
                return visitor.visitChildren(self)




    def expr_9(self):

        localctx = D96Parser.Expr_9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr_9)
        try:
            self.state = 561
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 556
                self.expr_10()
                self.state = 557
                self.match(D96Parser.STATIC_GLOBAL_DOT)
                self.state = 558
                self.expr_10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 560
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_10" ):
                return visitor.visitExpr_10(self)
            else:
                return visitor.visitChildren(self)




    def expr_10(self):

        localctx = D96Parser.Expr_10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expr_10)
        try:
            self.state = 566
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 563
                self.match(D96Parser.NEW)
                self.state = 564
                self.expr_10()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_11" ):
                return visitor.visitExpr_11(self)
            else:
                return visitor.visitChildren(self)




    def expr_11(self):

        localctx = D96Parser.Expr_11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expr_11)
        self._la = 0 # Token type
        try:
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 568
                self.literals()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                self.method_invocate_expression()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 570
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 571
                _la = self._input.LA(1)
                if not(_la==D96Parser.ID or _la==D96Parser.DOLLAR_ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 572
                self.index_id()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 573
                self.indexed_array()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 574
                self.match(D96Parser.NULL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 575
                self.class_new_object()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 576
                self.identifier()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 577
                self.match(D96Parser.LP)
                self.state = 578
                self.expr()
                self.state = 579
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_dimensional_arrays" ):
                return visitor.visitMulti_dimensional_arrays(self)
            else:
                return visitor.visitChildren(self)




    def multi_dimensional_arrays(self):

        localctx = D96Parser.Multi_dimensional_arraysContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_multi_dimensional_arrays)
        self._la = 0 # Token type
        try:
            self.state = 603
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 583
                self.indexed_array()
                self.state = 588
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 584
                        self.match(D96Parser.COMMA)
                        self.state = 585
                        self.indexed_array() 
                    self.state = 590
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 591
                self.match(D96Parser.ARRAY)
                self.state = 592
                self.match(D96Parser.LP)
                self.state = 593
                self.multi_dimensional_arrays()
                self.state = 598
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.COMMA:
                    self.state = 594
                    self.match(D96Parser.COMMA)
                    self.state = 595
                    self.multi_dimensional_arrays()
                    self.state = 600
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 601
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexed_array" ):
                return visitor.visitIndexed_array(self)
            else:
                return visitor.visitChildren(self)




    def indexed_array(self):

        localctx = D96Parser.Indexed_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_indexed_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(D96Parser.ARRAY)
            self.state = 606
            self.match(D96Parser.LP)
            self.state = 607
            self.expr()
            self.state = 612
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 608
                self.match(D96Parser.COMMA)
                self.state = 609
                self.expr()
                self.state = 614
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 615
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
        self._predicates[43] = self.expr_2_sempred
        self._predicates[44] = self.expr_3_sempred
        self._predicates[45] = self.expr_4_sempred
        self._predicates[48] = self.expr_7_sempred
        self._predicates[49] = self.expr_8_sempred
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
         




