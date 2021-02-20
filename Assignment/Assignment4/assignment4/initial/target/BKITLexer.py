# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u0225\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\39\79\u017d\n9\f9\16")
        buf.write("9\u0180\139\59\u0182\n9\3:\3:\3:\3:\7:\u0188\n:\f:\16")
        buf.write(":\u018b\13:\3;\3;\3;\3;\7;\u0191\n;\f;\16;\u0194\13;\3")
        buf.write("<\3<\3<\5<\u0199\n<\3=\3=\3>\3>\5>\u019f\n>\3>\6>\u01a2")
        buf.write("\n>\r>\16>\u01a3\3?\6?\u01a7\n?\r?\16?\u01a8\3?\3?\7?")
        buf.write("\u01ad\n?\f?\16?\u01b0\13?\3?\5?\u01b3\n?\3?\6?\u01b6")
        buf.write("\n?\r?\16?\u01b7\3?\3?\5?\u01bc\n?\3@\3@\5@\u01c0\n@\3")
        buf.write("A\3A\3A\3B\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\5G\u01d2")
        buf.write("\nG\3H\3H\7H\u01d6\nH\fH\16H\u01d9\13H\3H\3H\3H\3I\3I")
        buf.write("\7I\u01e0\nI\fI\16I\u01e3\13I\3I\5I\u01e6\nI\3I\3I\3J")
        buf.write("\3J\7J\u01ec\nJ\fJ\16J\u01ef\13J\3J\3J\5J\u01f3\nJ\3J")
        buf.write("\3J\5J\u01f7\nJ\5J\u01f9\nJ\3J\7J\u01fc\nJ\fJ\16J\u01ff")
        buf.write("\13J\3J\3J\3J\3K\3K\3K\3K\3K\3K\3L\3L\3L\3L\7L\u020e\n")
        buf.write("L\fL\16L\u0211\13L\3M\3M\3N\3N\3N\7N\u0218\nN\fN\16N\u021b")
        buf.write("\13N\3O\6O\u021e\nO\rO\16O\u021f\3O\3O\3P\3P\4\u01fd\u020f")
        buf.write("\2Q\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write("\2s\2u\2w:y\2{\2};\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f<\u0091=\u0093>\u0095")
        buf.write("?\u0097@\u0099\2\u009bA\u009dB\u009fC\3\2\26\3\2\63;\3")
        buf.write("\2\62;\4\2ZZzz\4\2\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2")
        buf.write("\629\4\2GGgg\4\2--//\t\2))^^ddhhppttvv\3\2))\3\2$$\b\2")
        buf.write("\n\n\f\f\16\17$$))^^\7\3\n\n\f\f\16\17))^^\3\2^^\4\2C")
        buf.write("\\c|\3\2c|\4\2\62;aa\5\2\13\f\16\17\"\"\2\u0230\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2w\3\2")
        buf.write("\2\2\2}\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a1\3\2\2\2\5\u00a6")
        buf.write("\3\2\2\2\7\u00ac\3\2\2\2\t\u00b5\3\2\2\2\13\u00b8\3\2")
        buf.write("\2\2\r\u00bd\3\2\2\2\17\u00c4\3\2\2\2\21\u00cc\3\2\2\2")
        buf.write("\23\u00d2\3\2\2\2\25\u00d9\3\2\2\2\27\u00e2\3\2\2\2\31")
        buf.write("\u00e6\3\2\2\2\33\u00ef\3\2\2\2\35\u00f2\3\2\2\2\37\u00fc")
        buf.write("\3\2\2\2!\u0103\3\2\2\2#\u0108\3\2\2\2%\u010c\3\2\2\2")
        buf.write("\'\u0112\3\2\2\2)\u0117\3\2\2\2+\u011d\3\2\2\2-\u0123")
        buf.write("\3\2\2\2/\u0125\3\2\2\2\61\u0127\3\2\2\2\63\u012a\3\2")
        buf.write("\2\2\65\u012c\3\2\2\2\67\u012f\3\2\2\29\u0131\3\2\2\2")
        buf.write(";\u0134\3\2\2\2=\u0136\3\2\2\2?\u0139\3\2\2\2A\u013b\3")
        buf.write("\2\2\2C\u013d\3\2\2\2E\u0140\3\2\2\2G\u0143\3\2\2\2I\u0146")
        buf.write("\3\2\2\2K\u0149\3\2\2\2M\u014b\3\2\2\2O\u014d\3\2\2\2")
        buf.write("Q\u0150\3\2\2\2S\u0153\3\2\2\2U\u0157\3\2\2\2W\u015a\3")
        buf.write("\2\2\2Y\u015d\3\2\2\2[\u0161\3\2\2\2]\u0165\3\2\2\2_\u0167")
        buf.write("\3\2\2\2a\u0169\3\2\2\2c\u016b\3\2\2\2e\u016d\3\2\2\2")
        buf.write("g\u016f\3\2\2\2i\u0171\3\2\2\2k\u0173\3\2\2\2m\u0175\3")
        buf.write("\2\2\2o\u0177\3\2\2\2q\u0181\3\2\2\2s\u0183\3\2\2\2u\u018c")
        buf.write("\3\2\2\2w\u0198\3\2\2\2y\u019a\3\2\2\2{\u019c\3\2\2\2")
        buf.write("}\u01bb\3\2\2\2\177\u01bf\3\2\2\2\u0081\u01c1\3\2\2\2")
        buf.write("\u0083\u01c4\3\2\2\2\u0085\u01c7\3\2\2\2\u0087\u01c9\3")
        buf.write("\2\2\2\u0089\u01cb\3\2\2\2\u008b\u01cd\3\2\2\2\u008d\u01d1")
        buf.write("\3\2\2\2\u008f\u01d3\3\2\2\2\u0091\u01dd\3\2\2\2\u0093")
        buf.write("\u01e9\3\2\2\2\u0095\u0203\3\2\2\2\u0097\u0209\3\2\2\2")
        buf.write("\u0099\u0212\3\2\2\2\u009b\u0214\3\2\2\2\u009d\u021d\3")
        buf.write("\2\2\2\u009f\u0223\3\2\2\2\u00a1\u00a2\7D\2\2\u00a2\u00a3")
        buf.write("\7q\2\2\u00a3\u00a4\7f\2\2\u00a4\u00a5\7{\2\2\u00a5\4")
        buf.write("\3\2\2\2\u00a6\u00a7\7D\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9")
        buf.write("\7g\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7m\2\2\u00ab\6")
        buf.write("\3\2\2\2\u00ac\u00ad\7E\2\2\u00ad\u00ae\7q\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1\7k\2\2\u00b1\u00b2")
        buf.write("\7p\2\2\u00b2\u00b3\7w\2\2\u00b3\u00b4\7g\2\2\u00b4\b")
        buf.write("\3\2\2\2\u00b5\u00b6\7F\2\2\u00b6\u00b7\7q\2\2\u00b7\n")
        buf.write("\3\2\2\2\u00b8\u00b9\7G\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb")
        buf.write("\7u\2\2\u00bb\u00bc\7g\2\2\u00bc\f\3\2\2\2\u00bd\u00be")
        buf.write("\7G\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7K\2\2\u00c2\u00c3\7h\2\2\u00c3\16")
        buf.write("\3\2\2\2\u00c4\u00c5\7G\2\2\u00c5\u00c6\7p\2\2\u00c6\u00c7")
        buf.write("\7f\2\2\u00c7\u00c8\7D\2\2\u00c8\u00c9\7q\2\2\u00c9\u00ca")
        buf.write("\7f\2\2\u00ca\u00cb\7{\2\2\u00cb\20\3\2\2\2\u00cc\u00cd")
        buf.write("\7G\2\2\u00cd\u00ce\7p\2\2\u00ce\u00cf\7f\2\2\u00cf\u00d0")
        buf.write("\7K\2\2\u00d0\u00d1\7h\2\2\u00d1\22\3\2\2\2\u00d2\u00d3")
        buf.write("\7G\2\2\u00d3\u00d4\7p\2\2\u00d4\u00d5\7f\2\2\u00d5\u00d6")
        buf.write("\7H\2\2\u00d6\u00d7\7q\2\2\u00d7\u00d8\7t\2\2\u00d8\24")
        buf.write("\3\2\2\2\u00d9\u00da\7G\2\2\u00da\u00db\7p\2\2\u00db\u00dc")
        buf.write("\7f\2\2\u00dc\u00dd\7Y\2\2\u00dd\u00de\7j\2\2\u00de\u00df")
        buf.write("\7k\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7g\2\2\u00e1\26")
        buf.write("\3\2\2\2\u00e2\u00e3\7H\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5")
        buf.write("\7t\2\2\u00e5\30\3\2\2\2\u00e6\u00e7\7H\2\2\u00e7\u00e8")
        buf.write("\7w\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7e\2\2\u00ea\u00eb")
        buf.write("\7v\2\2\u00eb\u00ec\7k\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\32\3\2\2\2\u00ef\u00f0\7K\2\2\u00f0\u00f1")
        buf.write("\7h\2\2\u00f1\34\3\2\2\2\u00f2\u00f3\7R\2\2\u00f3\u00f4")
        buf.write("\7c\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7")
        buf.write("\7o\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa")
        buf.write("\7g\2\2\u00fa\u00fb\7t\2\2\u00fb\36\3\2\2\2\u00fc\u00fd")
        buf.write("\7T\2\2\u00fd\u00fe\7g\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100")
        buf.write("\7w\2\2\u0100\u0101\7t\2\2\u0101\u0102\7p\2\2\u0102 \3")
        buf.write("\2\2\2\u0103\u0104\7V\2\2\u0104\u0105\7j\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7p\2\2\u0107\"\3\2\2\2\u0108\u0109")
        buf.write("\7X\2\2\u0109\u010a\7c\2\2\u010a\u010b\7t\2\2\u010b$\3")
        buf.write("\2\2\2\u010c\u010d\7Y\2\2\u010d\u010e\7j\2\2\u010e\u010f")
        buf.write("\7k\2\2\u010f\u0110\7n\2\2\u0110\u0111\7g\2\2\u0111&\3")
        buf.write("\2\2\2\u0112\u0113\7V\2\2\u0113\u0114\7t\2\2\u0114\u0115")
        buf.write("\7w\2\2\u0115\u0116\7g\2\2\u0116(\3\2\2\2\u0117\u0118")
        buf.write("\7H\2\2\u0118\u0119\7c\2\2\u0119\u011a\7n\2\2\u011a\u011b")
        buf.write("\7u\2\2\u011b\u011c\7g\2\2\u011c*\3\2\2\2\u011d\u011e")
        buf.write("\7G\2\2\u011e\u011f\7p\2\2\u011f\u0120\7f\2\2\u0120\u0121")
        buf.write("\7F\2\2\u0121\u0122\7q\2\2\u0122,\3\2\2\2\u0123\u0124")
        buf.write("\7?\2\2\u0124.\3\2\2\2\u0125\u0126\7-\2\2\u0126\60\3\2")
        buf.write("\2\2\u0127\u0128\7-\2\2\u0128\u0129\7\60\2\2\u0129\62")
        buf.write("\3\2\2\2\u012a\u012b\7/\2\2\u012b\64\3\2\2\2\u012c\u012d")
        buf.write("\7/\2\2\u012d\u012e\7\60\2\2\u012e\66\3\2\2\2\u012f\u0130")
        buf.write("\7,\2\2\u01308\3\2\2\2\u0131\u0132\7,\2\2\u0132\u0133")
        buf.write("\7\60\2\2\u0133:\3\2\2\2\u0134\u0135\7^\2\2\u0135<\3\2")
        buf.write("\2\2\u0136\u0137\7^\2\2\u0137\u0138\7\60\2\2\u0138>\3")
        buf.write("\2\2\2\u0139\u013a\7\'\2\2\u013a@\3\2\2\2\u013b\u013c")
        buf.write("\7#\2\2\u013cB\3\2\2\2\u013d\u013e\7(\2\2\u013e\u013f")
        buf.write("\7(\2\2\u013fD\3\2\2\2\u0140\u0141\7~\2\2\u0141\u0142")
        buf.write("\7~\2\2\u0142F\3\2\2\2\u0143\u0144\7?\2\2\u0144\u0145")
        buf.write("\7?\2\2\u0145H\3\2\2\2\u0146\u0147\7#\2\2\u0147\u0148")
        buf.write("\7?\2\2\u0148J\3\2\2\2\u0149\u014a\7>\2\2\u014aL\3\2\2")
        buf.write("\2\u014b\u014c\7@\2\2\u014cN\3\2\2\2\u014d\u014e\7>\2")
        buf.write("\2\u014e\u014f\7?\2\2\u014fP\3\2\2\2\u0150\u0151\7@\2")
        buf.write("\2\u0151\u0152\7?\2\2\u0152R\3\2\2\2\u0153\u0154\7?\2")
        buf.write("\2\u0154\u0155\7\61\2\2\u0155\u0156\7?\2\2\u0156T\3\2")
        buf.write("\2\2\u0157\u0158\7>\2\2\u0158\u0159\7\60\2\2\u0159V\3")
        buf.write("\2\2\2\u015a\u015b\7@\2\2\u015b\u015c\7\60\2\2\u015cX")
        buf.write("\3\2\2\2\u015d\u015e\7>\2\2\u015e\u015f\7?\2\2\u015f\u0160")
        buf.write("\7\60\2\2\u0160Z\3\2\2\2\u0161\u0162\7@\2\2\u0162\u0163")
        buf.write("\7?\2\2\u0163\u0164\7\60\2\2\u0164\\\3\2\2\2\u0165\u0166")
        buf.write("\7*\2\2\u0166^\3\2\2\2\u0167\u0168\7+\2\2\u0168`\3\2\2")
        buf.write("\2\u0169\u016a\7]\2\2\u016ab\3\2\2\2\u016b\u016c\7_\2")
        buf.write("\2\u016cd\3\2\2\2\u016d\u016e\7<\2\2\u016ef\3\2\2\2\u016f")
        buf.write("\u0170\7\60\2\2\u0170h\3\2\2\2\u0171\u0172\7.\2\2\u0172")
        buf.write("j\3\2\2\2\u0173\u0174\7=\2\2\u0174l\3\2\2\2\u0175\u0176")
        buf.write("\7}\2\2\u0176n\3\2\2\2\u0177\u0178\7\177\2\2\u0178p\3")
        buf.write("\2\2\2\u0179\u0182\7\62\2\2\u017a\u017e\t\2\2\2\u017b")
        buf.write("\u017d\t\3\2\2\u017c\u017b\3\2\2\2\u017d\u0180\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0182\3")
        buf.write("\2\2\2\u0180\u017e\3\2\2\2\u0181\u0179\3\2\2\2\u0181\u017a")
        buf.write("\3\2\2\2\u0182r\3\2\2\2\u0183\u0184\7\62\2\2\u0184\u0185")
        buf.write("\t\4\2\2\u0185\u0189\t\5\2\2\u0186\u0188\t\6\2\2\u0187")
        buf.write("\u0186\3\2\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u018a\3\2\2\2\u018at\3\2\2\2\u018b\u0189\3\2\2")
        buf.write("\2\u018c\u018d\7\62\2\2\u018d\u018e\t\7\2\2\u018e\u0192")
        buf.write("\t\b\2\2\u018f\u0191\t\t\2\2\u0190\u018f\3\2\2\2\u0191")
        buf.write("\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3\2\2\2")
        buf.write("\u0193v\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0199\5q9\2")
        buf.write("\u0196\u0199\5s:\2\u0197\u0199\5u;\2\u0198\u0195\3\2\2")
        buf.write("\2\u0198\u0196\3\2\2\2\u0198\u0197\3\2\2\2\u0199x\3\2")
        buf.write("\2\2\u019a\u019b\t\3\2\2\u019bz\3\2\2\2\u019c\u019e\t")
        buf.write("\n\2\2\u019d\u019f\t\13\2\2\u019e\u019d\3\2\2\2\u019e")
        buf.write("\u019f\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u01a2\5y=\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4|\3\2\2\2\u01a5\u01a7\5y=\2")
        buf.write("\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ae")
        buf.write("\7\60\2\2\u01ab\u01ad\5y=\2\u01ac\u01ab\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01b2\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3\5")
        buf.write("{>\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01bc")
        buf.write("\3\2\2\2\u01b4\u01b6\5y=\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7")
        buf.write("\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9\u01ba\5{>\2\u01ba\u01bc\3\2\2\2\u01bb")
        buf.write("\u01a6\3\2\2\2\u01bb\u01b5\3\2\2\2\u01bc~\3\2\2\2\u01bd")
        buf.write("\u01c0\5\u0081A\2\u01be\u01c0\5\u0083B\2\u01bf\u01bd\3")
        buf.write("\2\2\2\u01bf\u01be\3\2\2\2\u01c0\u0080\3\2\2\2\u01c1\u01c2")
        buf.write("\7^\2\2\u01c2\u01c3\t\f\2\2\u01c3\u0082\3\2\2\2\u01c4")
        buf.write("\u01c5\t\r\2\2\u01c5\u01c6\t\16\2\2\u01c6\u0084\3\2\2")
        buf.write("\2\u01c7\u01c8\t\f\2\2\u01c8\u0086\3\2\2\2\u01c9\u01ca")
        buf.write("\t\16\2\2\u01ca\u0088\3\2\2\2\u01cb\u01cc\n\f\2\2\u01cc")
        buf.write("\u008a\3\2\2\2\u01cd\u01ce\n\16\2\2\u01ce\u008c\3\2\2")
        buf.write("\2\u01cf\u01d2\n\17\2\2\u01d0\u01d2\5\177@\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2\u008e\3\2\2\2\u01d3")
        buf.write("\u01d7\7$\2\2\u01d4\u01d6\5\u008dG\2\u01d5\u01d4\3\2\2")
        buf.write("\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d8")
        buf.write("\3\2\2\2\u01d8\u01da\3\2\2\2\u01d9\u01d7\3\2\2\2\u01da")
        buf.write("\u01db\7$\2\2\u01db\u01dc\bH\2\2\u01dc\u0090\3\2\2\2\u01dd")
        buf.write("\u01e1\7$\2\2\u01de\u01e0\5\u008dG\2\u01df\u01de\3\2\2")
        buf.write("\2\u01e0\u01e3\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e4")
        buf.write("\u01e6\t\20\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e7\3\2\2")
        buf.write("\2\u01e7\u01e8\bI\3\2\u01e8\u0092\3\2\2\2\u01e9\u01ed")
        buf.write("\7$\2\2\u01ea\u01ec\5\u008dG\2\u01eb\u01ea\3\2\2\2\u01ec")
        buf.write("\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2")
        buf.write("\u01ee\u01f8\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f2\t")
        buf.write("\21\2\2\u01f1\u01f3\5\u0089E\2\u01f2\u01f1\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u01f9\3\2\2\2\u01f4\u01f6\t\r\2\2")
        buf.write("\u01f5\u01f7\5\u008bF\2\u01f6\u01f5\3\2\2\2\u01f6\u01f7")
        buf.write("\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01f0\3\2\2\2\u01f8")
        buf.write("\u01f4\3\2\2\2\u01f9\u01fd\3\2\2\2\u01fa\u01fc\13\2\2")
        buf.write("\2\u01fb\u01fa\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff")
        buf.write("\u01fd\3\2\2\2\u0200\u0201\7$\2\2\u0201\u0202\bJ\4\2\u0202")
        buf.write("\u0094\3\2\2\2\u0203\u0204\5\u0097L\2\u0204\u0205\7,\2")
        buf.write("\2\u0205\u0206\7,\2\2\u0206\u0207\3\2\2\2\u0207\u0208")
        buf.write("\bK\5\2\u0208\u0096\3\2\2\2\u0209\u020a\7,\2\2\u020a\u020b")
        buf.write("\7,\2\2\u020b\u020f\3\2\2\2\u020c\u020e\13\2\2\2\u020d")
        buf.write("\u020c\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u0210\3\2\2\2")
        buf.write("\u020f\u020d\3\2\2\2\u0210\u0098\3\2\2\2\u0211\u020f\3")
        buf.write("\2\2\2\u0212\u0213\t\22\2\2\u0213\u009a\3\2\2\2\u0214")
        buf.write("\u0219\t\23\2\2\u0215\u0218\5\u0099M\2\u0216\u0218\t\24")
        buf.write("\2\2\u0217\u0215\3\2\2\2\u0217\u0216\3\2\2\2\u0218\u021b")
        buf.write("\3\2\2\2\u0219\u0217\3\2\2\2\u0219\u021a\3\2\2\2\u021a")
        buf.write("\u009c\3\2\2\2\u021b\u0219\3\2\2\2\u021c\u021e\t\25\2")
        buf.write("\2\u021d\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u021f\u0220\3\2\2\2\u0220\u0221\3\2\2\2\u0221")
        buf.write("\u0222\bO\5\2\u0222\u009e\3\2\2\2\u0223\u0224\13\2\2\2")
        buf.write("\u0224\u00a0\3\2\2\2\35\2\u017e\u0181\u0189\u0192\u0198")
        buf.write("\u019e\u01a3\u01a8\u01ae\u01b2\u01b7\u01bb\u01bf\u01d1")
        buf.write("\u01d7\u01e1\u01e5\u01ed\u01f2\u01f6\u01f8\u01fd\u020f")
        buf.write("\u0217\u0219\u021f\6\3H\2\3I\3\3J\4\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BODY = 1
    BREAK = 2
    CONTINUE = 3
    DO = 4
    ELSE = 5
    ELSEIF = 6
    ENDBODY = 7
    ENDIF = 8
    ENDFOR = 9
    ENDWHILE = 10
    FOR = 11
    FUNCTION = 12
    IF = 13
    PARAMETER = 14
    RETURN = 15
    THEN = 16
    VAR = 17
    WHILE = 18
    TRUE = 19
    FALSE = 20
    ENDDO = 21
    ASSIGN = 22
    ADD_INT = 23
    ADD_FLOAT = 24
    SUB_INT = 25
    SUB_FLOAT = 26
    MUL_INT = 27
    MUL_FLOAT = 28
    DIV_INT = 29
    DIV_FLOAT = 30
    INT_REMAINDER = 31
    NOT = 32
    AND = 33
    OR = 34
    EQUAL = 35
    NOT_EQUAL = 36
    LESS_THAN = 37
    GREATER_THAN = 38
    LESS_EQUAL = 39
    GREATER_EQUAL = 40
    NOT_EQUAL_FLOAT = 41
    LESS_THAN_FLOAT = 42
    GREATER_THAN_FLOAT = 43
    LESS_EQUAL_FLOAT = 44
    GREATER_EQUAL_FLOAT = 45
    LP = 46
    RP = 47
    LSB = 48
    LRB = 49
    COLON = 50
    DOT = 51
    COMMA = 52
    SEMI = 53
    LB = 54
    RB = 55
    INTEGER_LITERAL = 56
    FLOAT_LITERAL = 57
    STRING_LITERAL = 58
    UNCLOSE_STRING = 59
    ILLEGAL_ESCAPE = 60
    COMMENT = 61
    UNTERMINATED_COMMENT = 62
    IDENTIFIER = 63
    WS = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'True'", "'False'", "'EndDo'", "'='", "'+'", "'+.'", "'-'", 
            "'-.'", "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'=/='", 
            "'<.'", "'>.'", "'<=.'", "'>=.'", "'('", "')'", "'['", "']'", 
            "':'", "'.'", "','", "';'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
            "RETURN", "THEN", "VAR", "WHILE", "TRUE", "FALSE", "ENDDO", 
            "ASSIGN", "ADD_INT", "ADD_FLOAT", "SUB_INT", "SUB_FLOAT", "MUL_INT", 
            "MUL_FLOAT", "DIV_INT", "DIV_FLOAT", "INT_REMAINDER", "NOT", 
            "AND", "OR", "EQUAL", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", 
            "LESS_EQUAL", "GREATER_EQUAL", "NOT_EQUAL_FLOAT", "LESS_THAN_FLOAT", 
            "GREATER_THAN_FLOAT", "LESS_EQUAL_FLOAT", "GREATER_EQUAL_FLOAT", 
            "LP", "RP", "LSB", "LRB", "COLON", "DOT", "COMMA", "SEMI", "LB", 
            "RB", "INTEGER_LITERAL", "FLOAT_LITERAL", "STRING_LITERAL", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "COMMENT", "UNTERMINATED_COMMENT", 
            "IDENTIFIER", "WS", "ERROR_CHAR" ]

    ruleNames = [ "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                  "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", "IF", 
                  "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "ENDDO", "ASSIGN", "ADD_INT", "ADD_FLOAT", "SUB_INT", 
                  "SUB_FLOAT", "MUL_INT", "MUL_FLOAT", "DIV_INT", "DIV_FLOAT", 
                  "INT_REMAINDER", "NOT", "AND", "OR", "EQUAL", "NOT_EQUAL", 
                  "LESS_THAN", "GREATER_THAN", "LESS_EQUAL", "GREATER_EQUAL", 
                  "NOT_EQUAL_FLOAT", "LESS_THAN_FLOAT", "GREATER_THAN_FLOAT", 
                  "LESS_EQUAL_FLOAT", "GREATER_EQUAL_FLOAT", "LP", "RP", 
                  "LSB", "LRB", "COLON", "DOT", "COMMA", "SEMI", "LB", "RB", 
                  "DEC", "HEX", "OCT", "INTEGER_LITERAL", "DIGIT", "EXPONENT", 
                  "FLOAT_LITERAL", "ESCAPE_SEQUENCES", "ESCAPE_SEQUENCES_BACKSLASH", 
                  "ESCAPE_SEQUENCES_SINGLEQUOTE", "POSTFIX_ESCAPE_SEQUENCES_BACKSLASH", 
                  "POSTFIX_ESCAPE_SEQUENCES_SINGLEQUOTE", "NOT_POSTFIX_ESCAPE_SEQUENCES_BACKSLASH", 
                  "NOT_POSTFIX_ESCAPE_SEQUENCES_SINGLEQUOTE", "STRING_CHAR", 
                  "STRING_LITERAL", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "COMMENT", "UNTERMINATED_COMMENT", "LETTER", "IDENTIFIER", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[70] = self.STRING_LITERAL_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                #cắt từ 1->length-2
                self.text = self.text[1:-1]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                imposible = ["'",'\b','\f','\r','\n','\\']
                if(self.text[-1] in imposible): #EOF?
                    raise UncloseString(self.text[1:-1])
                else:
                    raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		for x in range(len(self.text)):
            			if self.text[x] == '\\':
            	  			if (self.text[x+1] == 'b') or (self.text[x+1] == 'f') or (self.text[x+1] == 'r'):
            				    continue
            	  			elif (self.text[x+1] == 'n') or (self.text[x+1] == 't') or (self.text[x+1] == '\'') or (self.text[x+1] == '\\'):
            				    continue
            	  			elif (x+2)==(len(self.text)):
            				    x=x-1
            				    break
            	  			else:
            				    break
            			elif self.text[x] == '\'':
            	  			if(self.text[x+1] == '"'):
            	  			    continue 
            	  			elif (x+2)==(len(self.text)):
            				    x=x-1
            				    break
            	  			else:
            				    break                                      
            		raise IllegalEscape(self.text[1:x+2])

     


