# Editor's report

Laurence J. Golding and Michael Fanning

Presented at TC Meeting #7, November 29, 2017


1. The formal spec language for the following issues was made available for review after the last TC meeting (meeting #6), and we will move for their adoption in today's meeting:
 
    1. Issue [#27](https://github.com/oasis-tcs/sarif-spec/issues/27): "Add a help property to rule"

        Change draft: `Documents/ChangeDrafts/sarif-v1.0-issue-27-rule-help.docx`

    2. Issue [#56](https://github.com/oasis-tcs/sarif-spec/issues/27): "Consider adding namepaces to tags"

        Change draft: `Documents/ChangeDrafts/sarif-v1.0-issue-56-namespaced-tags-with-metadata.docx`

2. Based on the discussions so far, formal spec language for the following issues will be available by the next TC meeting. The editors will send mail to the TC distribution list as the "change draft" for each change becomes available:

    1. Issue [#33](https://github.com/oasis-tcs/sarif-spec/issues/33): "Should we allow formatting in messages?"
    
        The spec language will enable messages to contain rich text in any markup language, with GitHub-flavored markdown being the default.

    2. Issue [#61](https://github.com/oasis-tcs/sarif-spec/issues/61): "Consider specifying a format for links embedded in our plain text messages."

        The spec language will specify a syntax `[<link text>](<link target>)`, where `<link target>` is an integer that identifies any location mentioned in the `result` object (either a "related location", a code flow location, or a stack frame location).

        The spec language will permit these links _both_ in plain text message and in "rich" messages.

    3. Issue [#58](https://github.com/oasis-tcs/sarif-spec/issues/58): "Consider adding 'rank' or 'probability' property"

        The spec will define a property `result.rank`, in the range from 0.0 (lowest rank) to 1.0 (highest rank). The spec will recommend that tools whose "ranking values" cannot be converted to this range (for example, because they do not define an upper bound on the rank value) place their ranking value in the result's property bag.

3. Issue [#25](https://github.com/oasis-tcs/sarif-spec/issues/25): "One of result.{message,formattedRuleMessage} is required"

    We have made an editorial change to Sections 3.17.5 (`rule.message` property) and 3.17.6 (`rule.formattedRuleMessage` property) to clarify that at least one of them is required, but if they are both present, the `formattedRuleMessage` must resolve to the same text as the `message`.

    Change draft: `Documents/ChangeDrafts/sarif-v1.0-issue-25-message-formattedMessage.docx`