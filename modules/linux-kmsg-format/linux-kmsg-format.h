/*
 * Copyright (c) 2012 BalaBit IT Ltd, Budapest, Hungary
 * Copyright (c) 2012 Gergely Nagy <algernon@balabit.hu>
 *
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License version 2 as published
 * by the Free Software Foundation, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
 */

#ifndef LINUX_KMSG_FORMAT_H_INCLUDED
#define LINUX_KMSG_FORMAT_H_INCLUDED

#include "msg-format.h"

void linux_kmsg_format_handler(const MsgFormatOptions *parse_options,
                               const guchar *data, gsize length,
                               LogMessage *self);

void linux_msg_format_init (void);

#endif
