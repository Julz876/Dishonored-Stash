## 📥 How to Install in Blender (For Users)

1. In Blender 5.2+, go to **Edit > Preferences > Asset Libraries**.
2. Click the **`+`** icon at the top right of the table and select **Add Remote Asset Library**.
3. Enter library details:
   * **Name:** `<Library Name>`
   * **URL:** `https://julz876.github.io/Dishonored-Stash/`
4. Open the **Asset Browser** editor window (or press `Shift + F1`) and select your library from the top-left dropdown.

---

## ⚙️ Recommended Import Method: **Append**

When pulling assets into a scene:
* Set the **Import Method** in the Asset Browser header to **`Append`** (or **`Append (Reuse Data)`**).
* **Why?** Remote assets stream on demand. Using **Append** brings an independent, fully editable copy of shader graphs, Geometry Node trees, and mesh data directly into the active project file, preventing broken links if the scene is moved or shared.

---

> **Credit:**
* `augury-b` - Repo template
* FH Modding Server
* id-daemon

---
