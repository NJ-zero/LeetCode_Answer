# coding=utf-8
# author='Shichao-Dong'
# create time: 2019/3/5 

'''
罗马数字转整数
'''

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,
                   'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        sp=['IV','IX','XL','XC','CD','CM']
        if s=='IV':
            return 4
        elif s=='IX':
            return 9
        elif s=='XL':
            return 40
        elif s=='XC':
            return 90
        elif s=='CD':
            return 400
        elif s=='CM':
            return 900
        else:
            sum=0
            for ss in sp:
                if ss in s:
                    c=s.count(ss)
                    sum+=c*roman_dic[ss]
                    s=s.replace(ss,'')
                    print(s)
            for i in s:
                if i in roman_dic:
                    sum+=roman_dic[i]
            return sum
if __name__=="__main__":
    s=Solution()
    a="MCMXCIV"
    print(s.romanToInt(a))
    aa='abc'
    bb='ccabcddd'
    print(aa in bb)
    print(bb.count(aa))
    print(bb.replace(aa,''))

    s=[u'02743005321bcd46d2afee4f01f45bc3', u'dc0487390ebe320cb9f1754e7a05e8af', u'7811f106470f67d423cf2d2d0a93957b', u'86b0d9a9f8c42614b4c0604c8952a5ba', u'5e9d66ca608aa293ad27ae4211c71da8', u'70e4a3506785c3171703ce090c7412d0', u'fdb78c05a5060a3edace6f1c46143b5b', u'4231ffd87cc78b758ace348b05323482', u'3ac8a37e14be7334a1512c69144c8e65', u'cc8c3a0230699cf8532b2d3277e9dfe4', u'5d5af377b94a3b8038c73fd8a002195c', u'93b95d7d13191dbc89c3211a9911c740', u'47b652da49fba0171ad45afbfd339204', u'5c0236983d32be88cf38f90411ccfc54', u'735b8f1b35fd683119cd17fa5111b456', u'41e55f7df55f8a687ce97b847e6da6eb', u'322c40c050a83ebadb8d05214a74d2df', u'dadcfd4c3af6bb0697f49fb38ad72564', u'5899a12a9f84f94078c1001d5af8dfe3', u'5820022d81e148b7704777fdb5646519', u'21d5e2f2f80eaf80e4bfe5b402bf2e83', u'2cedb92c49da433605779adbc9b55c90', u'184f840a8857a5a3beb98c42fb2270dd', u'd4246e93f57e165f61e60329667831a1', u'30ea8683a82f64fd5cc75a06f09f2f75', u'bd886a3a25c194885acb5efe64745082', u'a6260a0bb056f2e5925bfb6175244431', u'e5237b57933484c08d8f5a30d337f0d0', u'9209172ecada0b22dd13710dbb6699a2', u'a9e51590edadaab63e55e2aec7cc7d23', u'bc2cfaf0aa7824e26b81e18fa7325968', u'801a949ea3a97ff96fdd61a1649b6b79', u'd064a77b315d033e0693fe303b747845', u'e7fe69dd03b639cf3622dffd6da11c83', u'f520ae2b52303585852c43ec99eb97c9', u'1699620ab73d2b5a7c2ead9997bc5a2f', u'0123f8ca3ffa68e15936cbc8c26043e0', u'193c47ca67ad243306594be7a4718db2', u'0a9546061e8ecf8241658fdad5a5cd90', u'1b9bd62a521262c6cffafa553aefba50', u'ffa7e99ad4eb9f46c8f81f5f76c6e5f4', u'0782aa6ce4a9438c5777311a57a8618d', u'7dab999c1696aab3758eef33b955728e', u'4270e0c8d49c68041abcb27f995c752c', u'390c8d6b14478ac3768c0b2032e3b51a', u'abb123656cf5847f43cb9c861b6c879f', u'5474794f6b23e2f165b200251e6d8122', u'84e55156b5850d75e1d525413750619b', u'ce0166271719d0972f41dcaeb114d397', u'db35f642f7afb6e70276cd159ec2ff1a', u'bf1e1309c186bfbfbc2a17029cdd1f6f', u'b2120a15a5a69c7d3088ba8a722f18e9', u'2767e09b53830605fac1075cf9ba8b35', u'0ca08088fde366b41179dfa644e6fcb7', u'1d9ea899e678f7ffd5d1e5447d9efb3b', u'3d1715819fd9843ff7e68c8cede7f714', u'1dc4e446b1508a4b6230427732ebc68b', u'b66475a69788f9ac73e900107a8e071c', u'c8018793c7077855469a1c41ab9933b1', u'94e72d90af48ecda1fa3066247524170', u'7811f106470f67d423cf2d2d0a93957b', u'cc8c3a0230699cf8532b2d3277e9dfe4', u'd453472ef7c904092ecdfbd81455bd3f', u'390c8d6b14478ac3768c0b2032e3b51a', u'2f7e62146f63da411a7bb83a13862b21', u'abb123656cf5847f43cb9c861b6c879f', u'bf1e1309c186bfbfbc2a17029cdd1f6f', u'0ca08088fde366b41179dfa644e6fcb7', u'3d1715819fd9843ff7e68c8cede7f714', u'e113e39d849edf2b00f56814d7d6152e', u'35dd0721d3cdc972cc509e922b1470bb', u'3e5011bfa0895dc1ebe76f3771db51fb', u'9142a79e98b7a885f941a67eaecd9de1', u'82569e238d351a3863f355cb00c1a009', u'f635ba6dcc086c906758dd3f003b269e', u'1df142563d5bf996970728b550577f4d', u'554a6a0e970e417043452734a38ab5dc', u'cbf0ad0ab584d0f6219cbe0300e46468', u'666822181de2bf59bfd4134362148718', u'c641b20bbc5ad053303acd968c240905', u'a92394457da019b341b938c2f0c32aad', u'8cd94552abf9e3b9ea1a4ac7c7ea27b9', u'06d3d4d42273827d2e9831d935778bb7', u'a3307185643c0a73c15c2bb070212aa2', u'c706b5801fb99c39087729ca66b72ac5', u'49ce809f8c0913a7b6f9100c58505875', u'd0a77c9497e801e7135874e65f6bab1f', u'9176ff9d7b5475273a7053a988b57266', u'd4327fd78d39156fcb80ca81cf9c70fc', u'e8a0f07b5797e7e1ea6132639936325e', u'326ba40cf8ae7d07dc1687e5b4cb7c9e', u'8a03ea80a6e2ffd87075452f8abfd360', u'5539e8b52e096f9dd59591b9829f33a6', u'd0d57be6c3baa79a391356dc16e87b20', u'5af1f285af9dcf02654a2b39483b8d49', u'a329e19adddfe4bbdd3549509c872f4e', u'd2cc24c677e040f7c479ed65aa07a1b5', u'f7f7fdd0702ccbfca56201fa2a463eae', u'd37a8a0ba1fdb75c7abb609d9c9b9e9d', u'af0fd21244950b698027a37c75c8ddab']
    print(len(s))
    new_s = list(set(s))
    print(len(new_s))
    for i in new_s:
        if s.count(i)>1:
            print(i)
