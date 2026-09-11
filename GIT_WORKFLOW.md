# Git workflow

Tài liệu này quy định cách cộng tác trên repository TalentScreen AI. Mục tiêu là
giữ `main` và `develop` luôn có thể build, kiểm thử và triển khai.

## Mô hình nhánh

| Nhánh | Mục đích | Push trực tiếp |
| --- | --- | --- |
| `main` | Mã đã được chấp thuận để release | Không |
| `develop` | Nhánh tích hợp cho đợt phát triển tiếp theo | Không |
| `feature/<slug>` | Tính năng mới | Chỉ người phụ trách |
| `fix/<slug>` | Sửa lỗi thông thường | Chỉ người phụ trách |
| `hotfix/<slug>` | Sửa lỗi production khẩn cấp | Chỉ người phụ trách |
| `docs/<slug>` | Thay đổi chỉ liên quan tài liệu | Chỉ người phụ trách |

Dùng chữ thường và dấu gạch ngang, ví dụ `feature/firebase-login` hoặc
`fix/multipart-boundary`.

## Quy trình hằng ngày

Tạo nhánh mới từ `develop` đã cập nhật:

```bash
git switch develop
git pull --ff-only origin develop
git switch -c feature/short-description
```

Trong quá trình làm việc:

```bash
git status --short
git diff
git add path/to/file
git commit -m "feat(scope): concise description"
```

Đồng bộ với nhánh tích hợp trước khi mở pull request:

```bash
git fetch origin
git rebase origin/develop
git push --set-upstream origin feature/short-description
```

Nếu nhánh đã được chia sẻ và cần cập nhật sau rebase, chỉ dùng
`git push --force-with-lease`; không dùng `--force`.

## Commit convention

Sử dụng Conventional Commits:

| Type | Khi sử dụng |
| --- | --- |
| `feat` | Thêm hành vi hoặc khả năng mới |
| `fix` | Sửa lỗi |
| `refactor` | Đổi cấu trúc mà không đổi hành vi |
| `docs` | Chỉ thay đổi tài liệu |
| `test` | Thêm hoặc sửa test |
| `perf` | Cải thiện hiệu năng |
| `build` | Build system hoặc dependency |
| `ci` | Pipeline và automation |
| `chore` | Công việc bảo trì khác |

Định dạng khuyến nghị:

```text
<type>(<scope>): <mô tả ngắn ở thể mệnh lệnh>
```

Ví dụ:

```text
feat(auth): add Firebase HR registration
fix(api): preserve multipart boundary in BFF proxy
docs(readme): clarify PostgreSQL local setup
```

Mỗi commit nên có một mục đích có thể review độc lập. Không trộn formatting,
refactor và thay đổi hành vi không liên quan trong cùng commit.

## Pull request

Mỗi pull request phải có:

- mô tả vấn đề và giải pháp;
- phạm vi thay đổi và phần cố ý không thay đổi;
- cách kiểm thử, kèm lệnh hoặc bằng chứng;
- migration, environment variable hoặc compatibility impact nếu có;
- ảnh hoặc video cho thay đổi UI đáng kể;
- liên kết issue/task liên quan.

Điều kiện merge:

1. Có ít nhất một reviewer khác approve.
2. Các status check bắt buộc đều pass.
3. Không còn conversation chưa được xử lý.
4. Nhánh không xung đột với target branch.
5. Tài liệu và migration được cập nhật cùng code nếu contract thay đổi.

Ưu tiên squash merge cho nhánh có nhiều commit sửa vặt; giữ commit riêng khi
lịch sử từng bước có giá trị vận hành hoặc migration.

## Hotfix production

Tạo hotfix từ `main`:

```bash
git switch main
git pull --ff-only origin main
git switch -c hotfix/short-description
```

Sau khi pull request vào `main` được merge và release đã xác minh, tạo pull
request đưa cùng thay đổi trở lại `develop`. Không bỏ qua bước này vì lỗi sẽ tái
xuất hiện ở release tiếp theo.

## Branch protection

Áp dụng cho cả `main` và `develop`:

- yêu cầu pull request trước khi merge;
- yêu cầu tối thiểu một approval;
- yêu cầu status checks pass và branch cập nhật;
- từ chối force-push và xóa nhánh;
- yêu cầu xử lý hết review conversations;
- giới hạn quyền bypass cho maintainer được chỉ định.

Tên status check phải khớp pipeline hiện hành trong `.github/workflows/` hoặc
`.gitlab-ci.yml`.

## Xử lý secret và dữ liệu nhạy cảm

- Không commit `.env`, API key, Firebase Admin credential, CV thật hoặc artifact
  chứa PII.
- Nếu secret đã vào lịch sử Git, việc xóa file ở commit mới là chưa đủ: phải
  rotate secret và thực hiện quy trình làm sạch lịch sử được maintainer phê duyệt.
- Không đưa raw provider response hoặc dữ liệu ứng viên vào pull-request log.

## Checklist trước khi push

- [ ] `git diff --check` không báo whitespace error.
- [ ] Chỉ stage file thuộc phạm vi task.
- [ ] Test và lint phù hợp đã chạy.
- [ ] Không có secret hoặc dữ liệu thật trong diff.
- [ ] Commit message tuân thủ convention.
- [ ] README/API/schema đã cập nhật nếu contract thay đổi.
