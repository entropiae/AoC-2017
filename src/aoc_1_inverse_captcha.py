def inverse_captcha_next(in_str):
    """
    The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that
    match the next digit in the list.
    The list is circular, so the digit after the last digit is the first digit in the list.

    What is the solution to your captcha?
    """
    def get_reference_char(idx):
        return get_element_in_position(idx + 1, in_str)

    return _inverse_captcha(in_str, get_reference_char)


def inverse_captcha_halfway(in_str):
    """
    Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.
    That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 s
    teps forward matches it. Fortunately, your list has an even number of elements.

    What is the solution to your new captcha?
    """
    def get_reference_char(idx):
        return get_element_in_position(idx + int(len(in_str) / 2), in_str)

    return _inverse_captcha(in_str, get_reference_char)


def get_element_in_position(idx, xs):
    while idx >= len(xs):
        idx %= len(xs)

    return xs[idx]


def _inverse_captcha(in_str, get_ref_char):
    return sum(int(c) for idx, c in enumerate(in_str) if c == get_ref_char(idx))


if __name__ == '__main__':
    input_string = '9384274494683632359351641411374573466273164687337536769779487433749179185568461296233353611992672753778126935276769885424719553291616136172298883156626254151278852582397949697874462178536295341822137377563322815527592267791213115418635363174876132196234374887626324931371241841242873783493835919238421879116421481543826222278152238576762132577763214642569545298668935216911493462229629786978273548147171384321525952959196377728493632872618291183256888417779495124837828187298244786175872713299271766246696631257484453347125176233373232245382158656142179687576388951175953419286858673221138553912229576523123114871637487978775855777483921896568333282333137175739746234262744256254149233843517254613981476355147487975859685936527161737644929119345127273149762325158784595946931447738173246311763677997888425452294562823751136515271874725143582623717324394587398371298523368386595426714148717735345237657249712685895921433468949182235146698174393928288313985355769799485511749423552935992391624424575278333625476148888355716967628454862834463357834291788479677576561681171516128495737923155533438413156639155128831349894646317546536886319328573512622325789672115171618195548534941184939233914166432349321992879287349932819135919518955561456615989137221875483561599493342981595678961836562435436285673764213941758954489582656271121429555455368545289416981624961261963953364918377483776322142975937971552271642224933926326665557787586927667898255947116988278131974381388514274833852552695679713424836536348449273149415872522111522749448188993159814183411853994579147867385867619467777654943169814287928966652552129439822741856512265955664872454951159255617513136142717471774698224566543617595742753244142364438589729356939483387466363477224283477843889679221229344974441624448489853764111425798141258155246636844914711222931548722647298953744242682551562166463942694715631497895981643174194294826868561578586851326262619731272665397711381459745281218196515155917877694663186732599688912878149242688741584822831861748845817871681621697944472377688658368145698614861456518138376989688166921187224726942589996534179549171859786241718727295379'
    next_result = inverse_captcha_next(input_string)
    print(f'Result for Part 1: {next_result}')
    halfway_result = inverse_captcha_halfway(input_string)
    print(f'Result for Part 2: {halfway_result}')
