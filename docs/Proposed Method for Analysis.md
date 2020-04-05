# Proposed Methods for Analysis and Points to Note

- Only tables prefixed with "Train" can be used since we do not have access to the test labels.
- Inpatient and Outpatient datasets seem very familiar, perhaps we can merge them together and then create a label indicating it's origin.
- If the final dataset is on a claim level, are we then stating that individual claims are fraudulent.
- Should we make the test data contain the more recent claims?

# Generating a Network

Under the premise that *Healthcare fraud is an organized crime which involves peers of providers, physicians, beneficiaries acting together to make fraud claims*, we may want to build a network (or many networks) that link using the following number of entities/nodes.

## Network 1

- Providers
- Physicians
- Beneficiaries
- Claim

These can be linked to each other in the following ways. We can also create a graph with just two node types Claims and transferrers (all else) - like GOTCHA (Bipartite Graph) and then perform a fraud exposure using PageRank.

- Can Providers be linked to a claim?
- Can Physician be linked to a claim?

| Edge Label    | End 1    | End 2  | Edge Definition |
| ------------- | -------- | ------ | --------------- |
| Claimed | Claim | Beneficiary | A claim is made by the beneficiary |
| Healed ??      | Beneficiary      | Physician | A physician was working on beneficiary |
| Employment | Physician | Providers | Physician works for provider ?? |
| Service | Beneficiary | Providers | Beneficiary got service from a provider |

## Network 2

- Claims

Since the dataset is on a claim level it may also be useful to have a graph of claims only to test. Claims can be linked to each other in the following ways.

| Edge Label    | Edge Definition |
| ------------- | --------------- |
| Beneficiary | Linked if claims are made by the same beneficiary |
| Physicians  | Linked if claims had the same physician (attending / operating / other) |
| Providers  | Linked if claims used the same providers |
