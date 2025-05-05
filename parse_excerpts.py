def load_excerpts(file_path="ellison-excerpts.md"):
    excerpts = []
    with open(file_path, "r", encoding="utf-8") as f:
        excerpt = {}
        for line in f:
            if line.startswith("###"):  # New excerpt
                if excerpt:
                    excerpts.append(excerpt)
                excerpt = {"title": line.strip("# ").strip(), "content": "", "tags": []}
            elif line.startswith("#"):  # Tags line
                excerpt["tags"] = [tag.strip() for tag in line.strip().split()]
            else:
                excerpt["content"] += line
        if excerpt:
            excerpts.append(excerpt)
    return excerpts
