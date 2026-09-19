def generate_grievance_letter(
    member_name,
    society_name,
    issue,
    relevant_rule
):

    letter = f"""
To,
The Secretary,
{society_name}

Subject: Grievance regarding {issue}

Respected Sir/Madam,

I, {member_name}, am a member of {society_name}.

I would like to raise a grievance regarding the following issue:

{issue}

Relevant rule/provision:

{relevant_rule}

I request that the matter be reviewed and appropriate action
be taken according to the applicable cooperative rules.

Thank you.

Yours faithfully,
{member_name}
"""

    return letter
