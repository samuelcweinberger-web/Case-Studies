# Custom Domain Setup (~10 minutes)

How to put this site on `samuelweinberger.com` (or a similar domain) instead of
`samuelcweinberger-web.github.io/Case-Studies/`.

## 1. Buy the domain (~5 min)

1. Go to a registrar — [Cloudflare Registrar](https://domains.cloudflare.com) (at-cost pricing, ~$10/yr) or [Namecheap](https://www.namecheap.com) are both good.
2. Search for `samuelweinberger.com`. If taken, try `samweinberger.com`, `samuelweinberger.me`, or `weinberger.io`.
3. Buy it. Skip all upsells (privacy protection is usually free and already included).

## 2. Point DNS at GitHub Pages (~3 min)

In your registrar's DNS settings for the domain, add these records:

| Type  | Name | Value |
|-------|------|-------|
| A     | `@`  | `185.199.108.153` |
| A     | `@`  | `185.199.109.153` |
| A     | `@`  | `185.199.110.153` |
| A     | `@`  | `185.199.111.153` |
| AAAA  | `@`  | `2606:50c0:8000::153` |
| AAAA  | `@`  | `2606:50c0:8001::153` |
| AAAA  | `@`  | `2606:50c0:8002::153` |
| AAAA  | `@`  | `2606:50c0:8003::153` |
| CNAME | `www` | `samuelcweinberger-web.github.io` |

(The AAAA records are optional but recommended — they enable IPv6.)

If you use Cloudflare, set the records to "DNS only" (gray cloud), not proxied,
at least until HTTPS is working.

## 3. Tell GitHub about the domain (~2 min)

1. Open the repo on GitHub → **Settings → Pages**.
2. Under **Custom domain**, enter `samuelweinberger.com` and click **Save**.
   - This commits a `CNAME` file (containing just the domain) to the repo root.
     Since `generate.py` never touches that file, it will survive regeneration.
3. Wait for the DNS check to pass (usually minutes; can take up to an hour).
4. Check **Enforce HTTPS** once it becomes available (GitHub provisions a
   Let's Encrypt certificate automatically).

## 4. Verify

- Visit `https://samuelweinberger.com` — the site should load at the root
  (no more `/Case-Studies/` path).
- Visit `https://www.samuelweinberger.com` — should redirect to the apex domain.

## Notes

- After the domain is live, update the `SITE_URL` constant at the top of
  `generate.py` to `https://samuelweinberger.com/` and re-run
  `python3 generate.py` so the Open Graph URLs and social-preview image point
  at the new domain.
- The old `github.io` URL keeps working — GitHub redirects it to the custom
  domain automatically.
