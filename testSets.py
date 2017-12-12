"""
Practicing some algebracis equations on sets
"""

def main():
    blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
    blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Josh'}
    smell_hcn = {'Harry', 'Amelia'}
    taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
    o_blood = {'Mia', 'Josh', 'Lily', 'Olivia'}
    b_blood = {'Amelia', 'Jack'}
    a_blood = {'Harry'}
    ab_blood = {'Mia', 'Lola'}

    # Test for Union (a or b)
    print(blue_eyes.union(blond_hair))

    # Test for intersection (a and b)
    print(smell_hcn.intersection(taste_ptc))

    # Test Difference
    print(smell_hcn.difference(b_blood))

    # Test symmetric difference
    print(blue_eyes.symmetric_difference(o_blood))

    # Test for subset
    print(ab_blood.issubset(taste_ptc))

if __name__ == '__main__':
    main()